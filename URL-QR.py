#Imports for python script

import pyfiglet
import png
import pyqrcode
import colorama
from colorama import Fore, Style
from termcolor import colored
import random
import string

banner = pyfiglet.figlet_format('URL-QR-GEN')
print(colored(banner, 'green'))

url = input("[*] Enter URL: ")
urlLength = len(url)
if urlLength > 4: 
    print(Fore.GREEN + "[*] Creating QR code for:  " + url +Style.RESET_ALL)

    genrate = pyqrcode.create(url)

    print(Fore.YELLOW + "[!] For a random file name press enter with no input" + Style.RESET_ALL)
    fileName = input("[*] Enter file name for QR code: ")
    fileNamelen  = len(fileName)
    if fileNamelen > 0:
        genrate.png(fileName + ".png", scale=5)
        print(Fore.GREEN +"[*] QR code successfully saved" + Style.RESET_ALL)
    else:
        randFileName = ''.join(random.choices(string.ascii_uppercase, k=8))
        genrate.png(randFileName + ".png", scale=5)
        print(Fore.GREEN +"[*] QR code successfully saved" + Style.RESET_ALL)     
else:
    print(Fore.RED + "[!] You must enter a URL.")
    print(Fore.RED + "[!] Program Closing." + Style.RESET_ALL)


    



