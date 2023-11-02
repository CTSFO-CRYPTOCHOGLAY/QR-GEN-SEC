#Imports for python script

import sys 
import os 
import pyfiglet
import png
import pyqrcode
import colorama
from colorama import Fore, Style
from termcolor import colored
import random
import string

# Program functions 

def successfulMessage():
    print(Fore.GREEN +"[*] QR code successfully saved" + Style.RESET_ALL)

def openingProgram():
    banner = pyfiglet.figlet_format('URL-QR-GEN')
    print(colored(banner, 'green'))

def closingProgram():
    print(Fore.RED + "[!] Program Closing." + Style.RESET_ALL)

def userURL():
   global url 
   url = input("[+] Enter URL: ")

def core(): 
    global urlLength
    urlLength = len(url)
    if urlLength > 4: 
        print(Fore.GREEN + "[*] Creating QR code for:  " + url +Style.RESET_ALL)

        genrate = pyqrcode.create(url)

        print(Fore.YELLOW + "[!] For a random file name press enter with no input" + Style.RESET_ALL)
        fileName = input("[+] Enter file name for QR code: ")
        fileNameExt = fileName + ".png" 
        if len(fileName) > 0:
            print("[+] File name: " + fileName + ".png")
        if os.path.isfile(fileNameExt):
            print(Fore.RED + "[!] File exists.")
            closingProgram()
        else:
            fileNamelen  = len(fileName)
            if fileNamelen > 0:
                    genrate.png(fileNameExt, scale=5)
                    successfulMessage()
            else:
                randFileName = ''.join(random.choices(string.ascii_uppercase, k=8))
                genrate.png(randFileName + ".png", scale=5)
                successfulMessage()
    else:
        print(Fore.RED + "[!] You must enter a URL.")
        closingProgram()


openingProgram()
userURL()
core()   