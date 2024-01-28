#Imports for python script
import json
import requests 
import argparse
import cv2
from pyzbar.pyzbar import decode
import sys 
import urllib.request
from urllib.error import HTTPError
import os 
import pyfiglet
import png
import pyqrcode
from colorama import Fore, Style
from termcolor import colored
import random
import string
import config 
   
# User Parser
userParser  = argparse.ArgumentParser()
userParser.add_argument("-f", "--function", help="[*] Select 1 of the 2 functions" and "python3 URL-QR.py -f URLQR",  type=str, choices=[ "URLQR", "qrReader", "help",])
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
    print("Reading & Security Scanning QR codes")
    print("[*] In order to reads QR codes use the qrReader option e.g. python3 NIDS_main.py -f qrReader")
    print("[*] Once started enter the path of the QR code that needs to be read.")
    print("[*] If the file is found and it contains a QR code it will read the QR code provied the info about it.")
    print("[*] If a URL is embbed within QR code you will have an option to run it aginst VT.")
    print("[*] Once scanned you will gain a report in the terminal if any postive matches where found.")

def websiteStatus(url):
    try:
        if "https://" in url:
            fullURL = url
        else:
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
    
def scan(URL):
    scanURL = URL

    payload = {
    "apikey": config.VirusTotalApiKey,
    "url": scanURL
}       
    headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}
    response = requests.post(config.totalVirusScanUrl, data=payload, headers=headers)
    responseData = response.text
    data = json.loads(responseData)
    scanId = data["scan_id"]

    params = { "apikey": config.VirusTotalApiKey, 'resource':scanId }
    response = requests.get(config.totalVirusReportUrl, params=params)
    Report = response.text

    dataReport = json.loads(Report)

    global scanID, resource, url, responseCode, scanDate, scanDate, permaLink, verboseMsg, filescanId, positives, total, scans

    scanID = dataReport["scan_id"] 
    resource = dataReport["resource"]
    url = dataReport["url"]
    responseCode = dataReport["response_code"]
    scanDate = dataReport["scan_date"]
    permaLink = dataReport["permalink"]
    verboseMsg = dataReport["verbose_msg"]
    filescanId = dataReport["filescan_id"]
    positives = dataReport["positives"]
    total = dataReport["total"]
    scans = dataReport["scans"]

    print("ScanID:", scanID)
    print("Resource: ", resource)
    print("Url:", url)
    print("Response Code:", responseCode)
    print("Scaned Date: ", scanDate)
    print("Perma Link:", permaLink)
    print("Verbose Msg:", verboseMsg)
    print("Filescan Id:", filescanId)
    print("Positives (Flagged By Vendor): ", positives)
    print("Total:",  total)
    scanedData = scans

    for scanName, scanResult in scanedData.items():
        detected = scanResult['detected']
        result = scanResult['result']
        print(f"Security vendor:  {scanName}:")
        print(f"Detected: {detected}")
        print(f"Result: {result}")
        print("-" * 20)

def readingQR():
    try:
        qrCodeFile = input(r"[*] Enter path of QR to be read: ")
        image = cv2.imread(qrCodeFile)
        decodedObjects = decode(image)
        for obj in decodedObjects:
            print(f"Data Contained In {obj.type}: {obj.data.decode('utf-8')}")
            global data 
            dataPulledfromQR = obj.data.decode('utf-8')

        userInput = input("[*] Do you want to run the URL though VirusTotal API(Y/N)?: ")
        apiLength = len(config.VirusTotalApiKey)
        if userInput == "Y":
            if apiLength > 30:
                scan(dataPulledfromQR)
            else:
                print(Fore.RED + "\n" + "[!] No API Key configured in config file." + Style.RESET_ALL)
                print("[*] Exited")  
        elif userInput == "N":
            print("[*] Exited")
    except KeyboardInterrupt:
            print(Fore.RED + "\n" + "[!] Operation interrupted by the user.")
            closingProgram()
   

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
    