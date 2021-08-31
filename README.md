# Poiana

**Reverse shell over TOR network using hidden services**

![](https://github.com/CalfCrusher/Poiana/blob/main/poiana.gif)

### Features

-> Create a hidden service

-> Generate non-staged payload (python/meterpreter_reverse_http)

-> Convert url using Tor2Web: a final extension .ws will be added, so url becomes available outside tor network

-> Generate batch .rc file for msfconsole

### Usage

NOTE: You need to edit your torrc file and insert: `ControlPort 9151`

I didn't want to insert this automatic 'feature' in my tool because of course you need to be root to edit torrc. In this way this script can run just as normal user. Remember do NOT run/trust scripts from others, discover some backdoor in fancy scripts is not rare unfortunately! Take care of source code, always :)

`$ git clone https://github.com/CalfCrusher/Poiana/`

`$ cd Poiana && pip3 install -r requirements.txt`

`$ python3 poiana.py`
 
## Why this project?

### Reverse Shell on hidden services through Tor are sexy

One of the weaknesses of the attackers when they're exfiltrating compromised information is that they
expose part of their technological infrastructure during the process. In this sense, the Tor network offers the possibility of making services in a machine accessible as hidden services, by taking advantage of the anonymity it offers and thereby preventing the real location of the machine from being exposed. Using Tor2Web, victim doesn't need to have tor or ncat. So, using Tor2Web our victim can establish a connection to our hidden service. To me it's really an interesting way to pop a reverse shell quite anonymously.

### Tor2Web

Tor2web https://www.tor2web.org - is a software project to allow Tor hidden services to be accessed from a standard browser without being connected to the Tor network. You can find a list of Tor2Web volunteers: https://www.reddit.com/r/onions/comments/bx19c6/list_of_tor2web_gateways/

### Disclaimer

**Onion network is NOT 100% bulletproof: https://www.wired.com/2014/12/fbi-metasploit-tor.
I made this tool just for educational use only. I'm not responsible for the consequences of illegal use. Please understands also that there is no warranty for this free software. Please note also that using Tor2Web is NOT secure from victim's point of view: the point of Tor is that users can connect without being eavesdropped on, and going through the clearnet (Tor2Web), even with https, seriously cripples the efforts made to protect users!**

*Be careful if the script fails to deleting hidden_service_data for some reasons. Script won't start correctly if this dir is already present before running tool. I'm trying to fix this behaviour, also because i want to add the (optional) feature to have persistence onion url and maybe the option to make a non-ephemeral hidden service (a hidden service without touching disk)*

