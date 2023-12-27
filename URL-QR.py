#Imports for python script
import vt
import requests 
import config 
import argparse
#from qrtools.qrtools import QR
import sys 
import urllib.request
from urllib.error import HTTPError
import os 
import pyfiglet
import png
import pyqrcode
import colorama
from colorama import Fore, Style
from termcolor import colored
import random
import string



def scan():
    scanURL = input("URL TEST: ") 

    payload = {
    "apikey": config.VirusTotalApiKey,
    "url": scanURL
}       
    headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}
    response = requests.post(config.totalVirusUrl, data=payload, headers=headers)
    print(response.text)
    
# User Parser
userParser  = argparse.ArgumentParser()
userParser.add_argument("-f", "--function", help="[*] Select 1 of the 2 functions" and "python3 URL-QR.py -f URLQR",  type=str, choices=[ "URLQR", "qrReader", "help", "SECScan"])
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
        try:
            status = urllib.request.urlopen(fullURL).getcode()
            if status == 200:
                core()
        except HTTPError as e:
            print(Fore.RED + "[!] HTTP Error: {e.code}" + Style.RESET_ALL)
            recall()
        except Exception as e:
            print(Fore.RED + "[!] An unexpected error occurred: {e}" + Style.RESET_ALL)
            recall()
    except KeyboardInterrupt:
        print(Fore.RED + "\n" + "[!] Operation interrupted by the user.")
        closingProgram()

def recall():
    usersCall = input(Fore.RED + "[!] Do you want to retry or bypass this check? (Y/N/B): " + Style.RESET_ALL)
    if usersCall == "Y":
        userURL()
    elif usersCall == "B":
        core()
    elif usersCall == "N":
        closingProgram()
    else:
        print(Fore.RED + "[!] Wrong Input Please Try Again" + Style.RESET_ALL)
        print(Fore.YELLOW + "[*] Y = Skip" + Style.RESET_ALL)
        print(Fore.YELLOW +"[*] N = Close Program" + Style.RESET_ALL)
        print(Fore.YELLOW +"[*] B = Bypass The URL Check" + Style.RESET_ALL)
        recall()

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

def folderCheck():
    try:
        folderName = "QRCODEs"
        # Check if the folder already exists
        if not os.path.exists(folderName):
            # Create the folder
            os.makedirs(folderName)
    except Exception as e:
        print("[!] An error occurred while creating the folder: {e}")
    

def readingQR():
    qrCodeFile = QR(filename=input(Fore.GREEN + "[*] Enter the path of the QR code with the file. " + Style.RESET_ALL))
    qrCodeFile.decode
    print(qrCodeFile.decode)

def core(): 
    try:
        urlLength = len(url)
        if urlLength > 4: 
            folderCheck() 
            print(Fore.GREEN + "[*] Creating QR code for:  " + url + Style.RESET_ALL)
            genrate = pyqrcode.create(url)
            print(Fore.YELLOW + "[!] For a random file name press enter with no input" + Style.RESET_ALL)
            fileName = input("[+] Enter file name for QR code: ")
            fileNameExt = fileName + ".png"
            
            savingPath = config.pathToSave if config.pathToSave else os.getcwd() + "/QRCODEs/"
            fileNameExt = fileName + ".png"
            fullPath = os.path.join(savingPath, fileNameExt)

            if os.path.isfile(fullPath):
                print(Fore.RED + "[!] File exists.")
                closingProgram()
            else:
                fileNamelen  = len(fileName)
                if fileNamelen > 0:
                        genrate.png(fullPath, scale=5)
                        successfulMessage(fileName)
                else:
                    randFileName = ''.join(random.choices(string.ascii_uppercase, k=8))
                    randFileNamePath = os.getcwd() + "/QRCODEs/" + randFileName
                    genrate.png(randFileNamePath + ".png", scale=5)
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
        readingQR()
    elif args.function == "help":
         help()
    elif args.function == "SECScan":
        scan()