import sys,os,subprocess

percorsoA='C:\\Users\\'+os.getlogin()+'\\AppData\\Local\\Programs\\MicrosoftDependency\\'
percorsoB='C:\\Users\\'+os.getlogin()+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Microsoft.pyw'

try: 
    os.remove(percorsoB)
except:
    print("ERRORE: appdata roaming cancellalo manualmente")
    subprocess.Popen('explorer "'+percorsoA+'"')
try: 
    os.remove(percorsoA)
except:
    print("ERRORE: appdata local cancellalo manualmente")
    subprocess.Popen('explorer "'+percorsoB+'"')

