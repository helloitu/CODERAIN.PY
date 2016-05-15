import os
import sys

print(""""

,---.         |     ,---.     o
|    ,---.,---|,---.|---',---..,---. ,---.,   .
|    |   ||   ||---'|  \ ,---|||   | |   ||   |
`---'`---'`---'`---'`   ``---^``   'o|---'`---|
                                     |    `---'

--------------------------------------------------
| [+] AUTOR:	Guilherme Cesar dos Santos       |
| [+] EMAIL:	gui.gui.guilhermec@hotmail.com   |
| [+] GITHUB:	github.com/helloitu              |
| [+] FACEBOOK:	fb.com/guilherme.cesar           |
--------------------------------------------------

""")

def main():
	install()



def install():

	print("1 = Install pentest tools")
	print("2 = List tools: ")
	print("3 = Quit")

	func = int(input("\033[1;36mOP: \033[1;m"))

	if func == 1:
		#repositorio
		os.system("echo '# Kali linux repositories |\ndeb http://http.kali.org/kali sana main non-free contrib\ndeb http://security.kali.org/kali-security sana/updates main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >> /etc/apt/sources.list")
		os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
		os.system("echo '# Backbox repositorios|\ndeb http://ppa.launchpad.net/backbox/four/ubuntu trusty main\ndeb-src http://ppa.launchpad.net/backbox/four/ubuntu trusty main' >> /etc/apt/sources.list")
		os.system('sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 78A7ABE1')
		os.system('sudo apt-get update -m')
		#Closed

		#Instalar
		os.system("sudo apt-get install bbqsql unix-privesc-check sqlmap dnschef armitage dotdotpwn fang john joomscan kismet amap armitage nmap zenmap tor fimap nikto setoolkit w3af vidalia torchat reaver ophcrack aircrack-ng beef wireshark hrex hydra")
		#

		#ListarTools
	elif func == 2:
		print("Armitage\nBBQSQL\nsqlmap\nAttest\nvidalia\nTorChat\nDnschef\nDotdotpwn\nFang\nJohn the rider\nJoomscan\nKismet\nAmap\nArmitage\nAtshell\nOwasp\nNmap\nZenmap\nTor\nFimap\nNikto\nSetoolkit\nOpenvas\nW3af\nChunch\nReaver\nOphcrack\nAircrack-ng\nBeef\nWireshark\nEtthercap\nHydra")

	elif func == 3:
		os.system("exit")


main()
