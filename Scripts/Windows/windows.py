import subprocess
import threading
import os
print('this is only to be used as admin')

def openTheWindows():
    #Auto-Updates Windows
    subprocess.call(r' wuauclt.exe /detectnow', shell = True)
    #will probably work on win 8, if not run powershell cmd below
    # subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","(New-Object -ComObject Microsoft.Update.AutoUpdate).DetectNow()" ";"])

def  findUsr():
    #finds currupt users and deletes them
