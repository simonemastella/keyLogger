import sys,os,subprocess
percorsoB='C:\\Users\\'+os.getlogin()+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'

try: 
    os.remove(percorsoB+"Microsoft.pyw")
except:
    print("ERRORE: appdata roaming cancellalo manualmente")
    subprocess.Popen('explorer "'+percorsoB+'"')


