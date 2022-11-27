import os
import time

os.system("clear")
os.system("figlet -f big BANNER | lolcat")
os.system("echo ---------------------------------------------")
a = input("\nEnter name:-")
os.system("clear")


os.system("figlet -f small PICKUP LINE | lolcat")
os.system("echo ---------------------------------------------")
c = input("\nEnter pickup line:-")
os.system("clear")
os.system("figlet -f small $")
os.system("echo ---------------------------------------------")
d = input("Dollar sign:-")
os.system("clear")


os.system("touch /data/data/com.termux/files/usr/etc/motd")
os.system("rm /data/data/com.termux/files/usr/etc/motd")
file =open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
file.write('figlet -f big '+a+' | lolcat \necho "'+c+'"\nshopt -s histappend\nshopt -s histverify\nexport HISTCONTROL=ignoreboth\nPROMPT_DIRTRIM=2\n\nPS1="\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\ '+d+'\[\e[0m\] "\nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n	command_not_found_handle() {\n		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"\n	}\nfi')

os.system("figlet -f small ADDING")
time.sleep(3)
print("Thanks Your Banner Was Added")
print("\nPlease Exit!")
print("‌ ")