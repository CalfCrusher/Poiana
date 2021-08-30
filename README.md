# Reverse shell on TOR network with hidden services

![](https://github.com/CalfCrusher/Poiana/blob/main/poiana.gif)

### Features

-> Create a hidden service

-> Generate non-staged payload (python/meterpreter_reverse_http)

-> Rewrite url using Tor2Web: a final extension .ws will be added, so url becomes available outside tor network

-> Generate batch .rc file for msfconsole

### Usage

`$ git clone https://github.com/CalfCrusher/Poiana/`

`$ cd Poiana && pip3 install -r requirements.txt`

`$ python3 poiana.py`
 
## Why this project?

### Reverse Shell on hidden services through Tor are sexy

One of the weaknesses of the attackers when they're exfiltrating compromised information is that they
expose part of their technological infrastructure during the process. In this sense, the Tor network offers the possibility of making services in a machine accessible as hidden services, by taking advantage of the anonymity it offers and thereby preventing the real location of the machine from being exposed. Using Tor2Web victim doesn't need to have tor or ncat compiled with ssl on his machine. So, using Tor2Web we can have a reverse shell connecting to our hidden service hiding our ip. To me it's really an interesting way to pop a reverse shell quite anonymously.

### Tor2Web

Tor2web https://www.tor2web.org - is a software project to allow Tor hidden services to be accessed from a standard browser without being connected to the Tor network. You can find a list of Tor2Web volunteers: https://www.reddit.com/r/onions/comments/bx19c6/list_of_tor2web_gateways/

### Disclaimer

***Onion network is NOT 100% bulletproof: https://www.wired.com/2014/12/fbi-metasploit-tor.
I made this tool just for educational use only. Please understands that there is no warranty for this free software. Please note also that using Tor2Web is NOT secure from victim's point of view: the point of Tor is that users can connect without being eavesdropped on, and going through the clearnet (Tor2Web), even with https, seriously cripples the efforts made to protect users!

