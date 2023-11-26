#Imports for python script

import argparse
#from qrtools.qrtools import QR
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
def updateMessage():
    print(Fore.RED + "[!] This feature is not available.")
    closingProgram()

def help():
    openingProgram()
    print("Program V1")
    print("Making QR codes")
    print("[*] The purpose of this tool is read and develop QR codes without the hassle of using 3rd party applications. Privacy matters!!")
    print("[*] In order to make QR codes use the URLQR option e.g. python3 NIDS_main.py -f URLQR")
    print("[*] The web url thats is passed has to be secure and online e.g.www.google.com")
    print("[*] When promted for a file name you can specify one or you instantly press enter to auto genrate a file name. All files are stored in current working directory.")
    print("")
    print("Reading QR codes")
    print("[*]")
    print("[*]")
    print("[*]")
    print("[*]")

def websiteStatus(url):
    try:
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
    except KeyboardInterrupt:
        print(Fore.RED + "\n" + "[!] Operation interrupted by the user.")
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
   try:
        url = input("[+] Enter URL: ")
        websiteStatus(url)
   except KeyboardInterrupt:
        print(Fore.RED + "\n" + "[!] Operation interrupted by the user.")
        closingProgram()

def readingQR():
    qrCodeFile = QR(filename=input(Fore.GREEN + "[*] Enter the path of the QR code with the file. " + Style.RESET_ALL))
    qrCodeFile.decode
    print(qrCodeFile.decode)

def core(): 
    try:
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
    except KeyboardInterrupt:
            print(Fore.RED + "\n" + "[!] Operation interrupted by the user.")
            closingProgram()

if __name__ == '__main__':
    if args.function == "URLQR":
        openingProgram()
        userURL()
    elif args.function == "qrReader":
        readingQR
    elif args.function == "help":
         help()

