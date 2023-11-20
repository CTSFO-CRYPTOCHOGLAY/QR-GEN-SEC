#Imports for python script

import argparse
import sys 
import urllib.request
import os 
import pyfiglet
import png
import pyqrcode
import colorama
from colorama import Fore, Style
from termcolor import colored
import random
import string

# User Parser
userParser  = argparse.ArgumentParser()
userParser.add_argument("-f", "--function", help="[*] Select 1 of the 2 functions" and "python3 NIDS_main.py -f URLQR",  type=str, choices=[ "URLQR", "qrReader", "help"])
args = userParser.parse_args()



# Program functions 

def websiteStatus(url):
    fullURL = "https://" + url 
    status = urllib.request.urlopen(fullURL).getcode()
    if status == 200:
        core()   
    else:
        error = input("This website does not produce a 200 code. Do you still want to continue? (Y/N)")
        if error.upper == "Y":
            core()  
        else:
            closingProgram()



def successfulMessage(passedFileName):
    print(Fore.GREEN +"[*] QR code successfully saveded as: " + passedFileName + ".png" + Style.RESET_ALL) 

def openingProgram():
    banner = pyfiglet.figlet_format('URL-QR-GEN')
    print(colored(banner, 'green'))

def closingProgram():
    print(Fore.RED + "[!] Program Closing." + Style.RESET_ALL)

def userURL():
   global url 
   url = input("[+] Enter URL: ")
   websiteStatus(url)

def core(): 
    urlLength = len(url)
    if urlLength > 4: 
        print(Fore.GREEN + "[*] Creating QR code for:  " + url + Style.RESET_ALL)

        genrate = pyqrcode.create(url)

        print(Fore.YELLOW + "[!] For a random file name press enter with no input" + Style.RESET_ALL)
        fileName = input("[+] Enter file name for QR code: ")
        fileNameExt = fileName + ".png" 
        if os.path.isfile(fileNameExt):
            print(Fore.RED + "[!] File exists.")
            closingProgram()
        else:
            fileNamelen  = len(fileName)
            if fileNamelen > 0:
                    genrate.png(fileNameExt, scale=5)
                    successfulMessage(fileName)
            else:
                randFileName = ''.join(random.choices(string.ascii_uppercase, k=8))
                genrate.png(randFileName + ".png", scale=5)
                successfulMessage(randFileName)
    else:
        print(Fore.RED + "[!] You must enter a URL.")
        closingProgram()

if __name__ == '__main__':
    if args.function == "URLQR":
        openingProgram()
        userURL()
    elif args.function == "qrReader":
         print(Fore.RED + "[!] This feature is not available.")
         closingProgram()
    elif args.function == "help":
         print(Fore.RED + "[!] This feature is not available.")
         closingProgram()

