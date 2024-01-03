# QR-GEN&SEC

## Description  
As well as focusing on making QR codes, there’s also a significant focus on security. In recent years, threat actors and criminals have been utilising QR codes for malicious operations, such as using web pages to deliver malware or harvesting information like PII, sensitive data or financial data.

The QR code reader developed employs a virus scan of the URL embedded in the QR code that has been statically decoded (so it will not be executed on the client side). This is powered by Virus Total (VT), so in order to get it working, an API key will be required by VT.

It’s vital to know that not all URLs are flagged by vendors, so always remain cautious, especially when QR codes are sent randomly to you being told to execute it, which is usually put in situations of urgency, curiosity and time sensitivity. 

## Installation

To downlaod the follwoing use the following commands below or downlaod zipped folder near the top right. 
Cick on 'Code' the green box and then the second option press "Download ZIP"   

```bash
git clone https://github.com/CTSFO-CRYPTOCHOGLAY/URL-QR-GEN
cd URL-QR-GEN
```

## Configuring the Configuration file

The purpose of the configuration is a separate file where you can set your VT API key.

Also, a path for saving QR codes can be set in this file instead of using the default path, which is as follows: 

Default Path::/PWD//QRCODEs/filename.png
PWD = (present working directory)

## Usage
To run the URL-QR-GEN script, ensure that Python 3 is being utilised or complications could occur. 

In order to run must be ran as SUDO or ROOT.
```bash
sudo python3 NIDS.py -f URLQR
sudo python3 NIDS.py -f qrReader
sudo python3 NIDS.py -f HELP
```

## Credits
The following URL-QR-GEN has been designed, developed and tested by Mohammed Choglay

## Licenses
All Rights Reserved
Created by Mohammed Ali Choglay
Version 1.0
