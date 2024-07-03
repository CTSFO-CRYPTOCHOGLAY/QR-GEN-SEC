# QR-GEN&SEC

## Description  
As well as focusing on making QR codes, there’s also a significant focus on security. In recent years, threat actors and criminals have been utilising QR codes for malicious operations, such as using web pages to deliver malware or harvesting information like PII, sensitive data or financial data.

The QR code reader developed employs a virus scan of the URL embedded in the QR code that has been statically decoded (so it will not be executed on the client side). This is powered by Virus Total (VT), so in order to get it working, an API key will be required by VT.

It’s vital to know that not all URLs are flagged by vendors, so always remain cautious, especially when QR codes are sent randomly to you, and you are being told to execute them by an unknown person. However, account compromises are on the rise where attackers will utilise real accounts they have taken over, so always be cautious and verify with the person through official channels. The situations are usually put in the following categories to increase the chance of attack these are as follow: 
* urgency
* Curiosity
* time sensitivity

## Installation

To downlaod the follwoing use the following commands below or downlaod zipped folder near the top right. 
Cick on 'Code' the green box and then the second option press "Download ZIP"   

```bash
git clone https://github.com/CTSFO-CRYPTOCHOGLAY/URL-QR-GEN
cd URL-QR-GEN
```

## Configuring the Configuration file

The purpose of the configuration is a separate file where you can set your VT API key.Also, a path for saving QR codes can be set in this file instead of using the default path, which is as follows: 

* Default Path: C:\PWD\QRCODEs\filename.png
* PWD = (present working directory)

### Obtaining VT API Key  

To obtain a  VT API key, head to https://www.virustotal.com/. Once on the web page, click sign up or sign in top right like shown below.

![image](https://github.com/CTSFO-CRYPTOCHOGLAY/QR-GEN-SEC/assets/72378816/2fd8e889-8319-476d-8002-065293748cca) 

Once logged in right click on your profile in the top right coner and select API Key.

![image](https://github.com/CTSFO-CRYPTOCHOGLAY/QR-GEN-SEC/assets/72378816/5a62d0e1-7321-41bd-ba4a-c70db9890739) 

Now, you can view your API key by pressing the eye icon. It's vital to know you should always keep your API key private for security reasons. 

![image](https://github.com/CTSFO-CRYPTOCHOGLAY/QR-GEN-SEC/assets/72378816/02b5b3f1-6ac8-4da5-9411-e62e8aa38f9f)




## Usage
To run the URL-QR-GEN script, ensure that Python 3 is being utilised or complications could occur. 

```bash
sudo python3 URL-QR.py -f URLQR
sudo python3 URL-QR.py -f qrReader
sudo python3 NIDS.py -f help
```

## Credits
The following URL-QR-GEN has been designed, developed and tested by Mohammed Choglay

## Licenses
All Rights Reserved
Created by Mohammed Ali Choglay
Version 1.0
