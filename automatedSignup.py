import pyautogui as pag
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
url = 'http://docs.python.org/'

screen_size = pag.size() # get resolution

emails = ["email1@domain.com", "email2@domain.com", "email3@domain.com", "email4@domain.com", "email5@domain.com", "email6@domain.com"]

for email in emails:
    webbrowser.get(chrome_path).open(url)
    pag.click(x=100, y=750)    
    pag.click(x=320, y=400)    
    pag.typewrite(email)               
    pag.press("enter")
    #pag.hotkey('ctrl', 'w')            #closes current tab
