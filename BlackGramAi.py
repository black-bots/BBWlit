#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Supreme Ciento"
__copyright__ = "Copyright 2023, Cloud Bots™ BlackBots"
__credits__ = ["Supreme Ciento"]
__license__ = "GPL"
__maintainer__ = "Cloud Bots™ BlackBots"
__email__ = "BlackBots@Techie.com"
__status__ = "Production"

__version__ = "6.6.21.0"

import win32com,win32com.client
shell=win32com.client.Dispatch('WScript.Shell')
import win32gui
Minimize=win32gui.FindWindow('ConsoleWindowClass','C:\\WINDOWS\\py.exe')
import win32con
try:win32gui.ShowWindow(Minimize,win32con.SW_MINIMIZE)
except:pass
from selenium import webdriver
from datetime import datetime
from time import sleep
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as Firefox_Options
from webdriverdownloader import GeckoDriverDownloader
import webbrowser
import random
import emoji
from random import randint
from threading import Thread
import PySimpleGUI as sg
import sys
import openai
import prompt_toolkit
import os
import pickle
import shutil
import ssl
import re

model=""

sg.ChangeLookAndFeel('DarkBlack') # change style

browser = ""

_b=r'Add Photos to Folder!!'
_a=r'Upload Folder(IGPhotos)'
_c='IGPhotos Folder NOT Found!'
_Z='About::-HELP-'
_Y='Emojis::-EMO-'
_X='Restart (Ctrl+N)'
_W='Open::-SUB-'
_V='BlackGram Upload'
_U='explorer .\\IGPhotos'
_T='__Next__'
_S='center'
_R='Courier New'
_Q='white'
_P='black'
_O='Error'
_N='-HB-'
_M='Consolas'
_L=None
_K='-CB-'
_J='__HASH__'
_I='__PASS__'
_H='__USER__'
_G='.\\IGPhotos'
_F='gold'
_E='lime'
_D=False
_C='_STLINE_'
_B='_INFO_'
B='gold'
_A=True

Hrt = ':red_heart:'
RA = emoji.emojize(':right_arrow:')
Rh = emoji.emojize(Hrt)
Rn = emoji.emojize(':person_running:')
Xx = emoji.emojize(':cross_mark:')
ZZ = emoji.emojize(':sleeping_face:')
ZZZ = emoji.emojize(':ZZZ:')


WIN_W = 27
WIN_H = 15

checked = b'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'
unchecked = b'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'
    
sg.set_options(auto_size_buttons=True,
            margins=(0, 0))
 
menu_layout = [
        ['File', ['Restart (Ctrl+N)', 'Exit']],
        ['Help', ['About::-HELP-']],
        ]

ColCent = [
        [sg.Text('Username', text_color='gold', size=(10, 1), key='__U__'), sg.InputText(font=('Consolas', 12), background_color="black", justification='LEFT', size=(12, 4), key='__USER__')],
        [sg.Text('Password', text_color='gold', size=(10, 1), key='__P__'), sg.InputText(font=('Consolas', 12), background_color="black", justification='LEFT', size=(12, 4), key='__PASS__', password_char='*')],
        [sg.Text('Focus Word', text_color='gold', size=(10, 1), key='__H__'), sg.InputText(font=('Consolas', 12), background_color="black", justification='LEFT', size=(12, 4), key='__HASH__')],
        [sg.Text('API-Key', text_color='gold', size=(10, 1), key='__A__'), sg.InputText(font=('Consolas', 12), background_color="black", justification='LEFT', size=(12, 4), key='__API__', password_char='*')],

        [sg.VPush()],
        [sg.Multiline("", no_scrollbar=True, visible=False, autoscroll=True, justification='center', font=('Courier New', 12), border_width=0 ,size=(WIN_W,2), key='_STLINE_', background_color='black')],
        [sg.Text('% to Like', text_color='gold', size=(12, 1), key='__L__'), sg.InputText(font=('Consolas', 12), background_color="black", justification='LEFT', size=(2, 4), key='__LIK__')],
        [sg.Text('% to Comment', text_color='gold', size=(12, 1), key='__C__'), sg.InputText(font=('Consolas', 12), background_color="black", justification='LEFT', size=(2, 4), key='__COM__')],
        [sg.Text('Hide?', text_color='gold', size=(8, 1), key='-CBT-'), sg.Text("" *5),sg.Checkbox("", default=False, key="-CB-", enable_events=True), sg.Text('', size=(7, 1), key='-HB-', justification='center', enable_events=True)],
        [sg.Text('Follow?', text_color='gold', size=(8, 1), key='-CBT2-'), sg.Text("" *5),sg.Checkbox("", default=False, key="-CB2-", enable_events=True), sg.Text('', size=(7, 1), key='-HB2-', justification='center', enable_events=True)],
        [sg.VPush()],
        [sg.Text('      (-START-)', font=('Courier New', 14), enable_events=True, text_color='white', key='__Next__'), sg.Text(font=('Lucida', 16), size=(4,4), key='C1', background_color=None)]
        ]

layout = [
        [sg.MenubarCustom(menu_layout, text_color='white', pad=((1,1),(1,1)), bar_text_color='gold', background_color='black')],
        [sg.Text('        > BlackGram <', text_color='gold', justification='center', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
        [sg.Push(), sg.Column(ColCent, element_justification='c')]
        ]

window = sg.Window('BlackGram', keep_on_top=True, layout=layout, margins=(0, 0), grab_anywhere=True, resizable=True, use_custom_titlebar=True, no_titlebar=True, return_keyboard_events=False, enable_close_attempted_event=True, finalize=True)
window['__USER__'].Widget.configure(highlightcolor='gold', highlightthickness=0.5)
window['__PASS__'].Widget.configure(highlightcolor='gold', highlightthickness=0.5)
window['__HASH__'].Widget.configure(highlightcolor='gold', highlightthickness=0.5)
window['__COM__'].Widget.configure(highlightcolor='gold', highlightthickness=0.5)
window['__LIK__'].Widget.configure(highlightcolor='gold', highlightthickness=0.5)
window['__API__'].Widget.configure(highlightcolor='gold', highlightthickness=0.5)

window['_STLINE_'].Widget.config(cursor=None)
window['_INFO_'].Widget.config(cursor=None)

def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(x, y)
    #usage  -  move_center(window)

def rsleep(self, minimum=1, maximum=5):
    t = randint(minimum, maximum)

    for remaining in range(5, 0, -1):
        window['_INFO_'].update(value="        Waiting {:2d} seconds -\n".format(remaining))
        sleep(1)
    sleep(t)

def threading():
    t = Thread(target=start, daemon=True)
    t.start()

posts=0
commentss=0
follows = 0

def start():
    window['_STLINE_'].update(value='Likes: ')
    window['_STLINE_'].update(value=str(posts), text_color_for_value='lime', append=True)
    window['_STLINE_'].update(value=' | ', text_color_for_value='gold', append=True)
    window['_STLINE_'].update(value='Comments: ', text_color_for_value='white', append=True)
    window['_STLINE_'].update(value=str(commentss), text_color_for_value='lime', append=True)
    window['_STLINE_'].update(value='\n  Follows: ', text_color_for_value='white', append=True)
    window['_STLINE_'].update(value=str(follows), text_color_for_value='lime', append=True)
    def generate_response(prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=3600,
            n=1,
            stop=None,
            temperature=1,
        )
        message = response.choices[0].text.strip()
        return message

    def Comment(browser):

        ai_comm = "Write a nice generic Instagram Photo comment pertaining to a pleasant picture and ask for whomever to checkout your instagram page which is " + username_str + "."
        comment = WebDriverWait(browser, 10).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, "_aamx")))
        comment.click()
        sleep(random.uniform(1, 5))
        try:
            commentin = WebDriverWait(browser, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea')))
        except:
            commentin = WebDriverWait(browser, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[3]/div/form/div/textarea')))
        comments = generate_response(ai_comm)
        commentin.send_keys(comments)
        commentin.send_keys(Keys.RETURN)
        window['_INFO_'].update(value="Comment +1")
        sleep(2)
    def likeAndComm(browser):
        global commentss
        global follows
        
        try:
            WebDriverWait(browser, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//button[text()='" + 'Not Now' + "']"))).click()
        except:
            pass
        
        count = 1
        n = 9
        
        ai_tag = "Write 1 line consisting of 2 to 5 synonyms for the word: " +word+ ". Seperate each word or phrase with a comma. Do not add any spaces before or after a word, only commas are permitted."
        hash_str = generate_response(ai_tag)

        hasht = str(hash_str)
        list = hasht.split(",")
        hashtags = list
        hashT = random.choice(hashtags)
        hashT = hashT.replace(' ', '')
        hashT = hashT.replace('"', '')
        hashT = hashT.replace('.', '')
        hashT = hashT.replace('-', '')
        browser.get('https://www.instagram.com/explore/tags/' + hashT)
        sleep(random.uniform(3, 10))
        global posts
        postss = 0
        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "_aagw"))).click()
        except:
            browser.get('https://www.instagram.com/explore/tags/' + hashT)
            sleep(7)
            likeAndComm(browser)
        while count in range(n):
            count += 1
            sleep(2)
            next(browser)
            sleep(2)
        window['_INFO_'].update(value="Deciding to Like or not..")                    
        while postss < 10:
            Lchance = random.randint(1,100)
            if Lchance <= int(x5):
                likeIt = WebDriverWait(browser, 10).until(
                                EC.visibility_of_element_located((By.CLASS_NAME, "_aamw")))
                color = likeIt.get_property("innerHTML")
                try:
                    if "#8e8e8e" not in color:
                        sleep(random.uniform(2, 4))
                        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "_aamw")))
                        likeIt.click()
                        window['_INFO_'].update(value="Post Liked")
                        sleep(random.uniform(2, 4))
                    else:
                        sleep(random.uniform(2, 4))
                except:
                    likeAndComm(browser)
            else:
                next(browser)
            window['_INFO_'].update(value="Trying to Comment..")
            sleep(random.uniform(2, 6))
            chance = random.randint(1,100)
            if chance <= int(x6):
                try:
                    Comment(browser)
                    window['_INFO_'].update(value="Post Commented")
                    commentss +=1

                except:
                    likeAndComm(browser)
            if chance <= int(x6):
                if values["-CB2-"] == True:
                    window['_INFO_'].update(value="Trying to Follow..")
                    follows+=1
                    try:
                        WebDriverWait(browser, 10).until(
                            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div"))).click()
                        sleep(random.uniform(2, 5))
                    except:
                        pass
                else:
                    pass
            else:
                pass
            posts+=1
            postss+=1

            window['_INFO_'].update(value="Waiting..")
            watin = sleep(random.uniform(10, 60))

            window['_INFO_'].update(value="Loading..")
            window['_STLINE_'].update(value='Likes: ')
            window['_STLINE_'].update(value=str(posts), text_color_for_value='lime', append=True)
            window['_STLINE_'].update(value=' | ', text_color_for_value='gold', append=True)
            window['_STLINE_'].update(value='Comments: ', text_color_for_value='white', append=True)
            window['_STLINE_'].update(value=str(commentss), text_color_for_value='lime', append=True)
            window['_STLINE_'].update(value='\n  Follows: ', text_color_for_value='white', append=True)
            window['_STLINE_'].update(value=str(follows), text_color_for_value='lime', append=True)
            next(browser)
        if postss >= 10:
            closePost=  WebDriverWait(browser, 10).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div')))
            closePost.click()
            postss = 0
        else:
            next(browser)
        window['_INFO_'].update(value=ZZ + ' Zzz')
        window['_STLINE_'].update(value='Sleeping..: ', text_color_for_value='gold')
        window['_STLINE_'].update(value='Likes: ', text_color_for_value='white', append=True)
        window['_STLINE_'].update(value=str(posts), text_color_for_value='lime', append=True)
        window['_STLINE_'].update(value=' | ', text_color_for_value='gold', append=True)
        window['_STLINE_'].update(value='Comments: ', text_color_for_value='white', append=True)
        window['_STLINE_'].update(value=str(commentss), text_color_for_value='lime', append=True)
        window['_STLINE_'].update(value='\n  Follows: ', text_color_for_value='white', append=True)
        window['_STLINE_'].update(value=str(follows), text_color_for_value='lime', append=True)

        sleep(random.uniform(300, 1200))

        likeAndComm(browser)
        
            
    def next(browser):
        window['_INFO_'].update(value=RA+'Next Post '+RA)
        next_path = "//*[@aria-label='Next']"
        WebDriverWait(browser, 7).until(
            EC.visibility_of_element_located((By.XPATH, next_path))).click()

        
    def launch_browser(path_to_chromedriver, images=True):
        try:
            chrome_options = webdriver.ChromeOptions()
            if images:
                chrome_options.add_experimental_option("prefs", {"intl.accept_languages": 'en,en_US'})
            else:
                chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2,
                                                                'intl.accept_languages': 'en,en_US'})
            chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
            chrome_options.add_experimental_option("useAutomationExtension", False) 
            chrome_options.add_argument('--dns-prefetch-disable')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--lang=en-US')
            chrome_options.add_argument('--disable-setuid-sandbox')
            chrome_options.add_argument("window-size=700,700")

            if values["-CB-"] == True:
                 chrome_options.add_argument("--headless")
                 chrome_options.add_argument("window-size=1000,700")
                 user_agent = "Chrome"
                 chrome_options.add_argument('user-agent={user_agent}'
                                             .format(user_agent=user_agent))
                 window['_INFO_'].update(value="Botting behind the scenes(Chrome)")
            browser = webdriver.Chrome(path_to_chromedriver, options=chrome_options)
            window['_INFO_'].update(value="Chrome Browser Selected")

        except:
            try:
                webdriver.quit()
                pass
            except:
                pass
            window['_INFO_'].update(value="Chrome not detected. Trying Firefox..")
            get_geckodriver()
            sleep(4)
            firefox_options = Firefox_Options()
            browser = webdriver.Firefox(executable_path="geckodriver.exe", options=firefox_options)
            window['_INFO_'].update(value="Firefox Browser Selected")
            if values["-CB-"] == True:
                 firefox_options.add_argument("--headless")
                 firefox_options.add_argument("window-size=1000,700")
                 user_agent = "Firefox"
                 chrome_options.add_argument('user-agent={user_agent}'
                                             .format(user_agent=user_agent))
                 window['_INFO_'].update(value="Botting behind the scenes(Firefox)")
        return browser

    def save_cookie(browser, username_str):
        sleep(3)
        if os.path.exists('Data/' + username_str):
            path = 'Data/' + username_str + '/cookies_file'
        else:
            os.makedirs('Data/' + username_str)
            path = 'Data/' + username_str + '/cookies_file'
        with open(path, 'wb') as filehandler:
            pickle.dump(browser.get_cookies(), filehandler)

    def SAVE_cookies(browser, username_str, password_str):
        sleep(3)
        save_cookie(browser, username_str)

    def load_cookie(browser, username_str):
        sleep(3)
        try:
            path = 'Data/' + username_str + '/cookies_file'
            with open(path, 'rb') as cookiesfile:
                cookies = pickle.load(cookiesfile)
                for cookie in cookies:
                    browser.add_cookie(cookie)
        except:
            pass
    def LOAD_cookie(browser, username_str):
        try:
            browser.get('https://www.instagram.com/')
            window['_INFO_'].update(value="Instagram.com")
            sleep(3)
            window['_INFO_'].update(value="Trying Cookie..")
            load_cookie(browser, username_str)
            browser.get('https://www.instagram.com/' + username_str)
            window['_INFO_'].update(value=username_str)
            browser.get('https://www.instagram.com/')
            sleep(3)
        except:
            pass
    def get_geckodriver():
        gecko_path = shutil.which("geckodriver") or shutil.which("geckodriver.exe")
        if gecko_path:
            return gecko_path

        owd = os.getcwd()
        os.chdir(owd)

        asset_path = owd
        gdd = GeckoDriverDownloader(asset_path, asset_path)
        sym_path = gdd.download_and_install()[1]
        return sym_path

    def Login():
        try:
            window['_INFO_'].update(value="Logging In..")
            sleep(random.uniform(2, 5))
            username = browser.find_element(By.NAME, 'username')
            username.send_keys(str(username_str))
            sleep(random.uniform(2, 4))
            password = browser.find_element(By.NAME, 'password')
            password.send_keys(password_str)
            submit = browser.find_element(By.TAG_NAME, "form")
            sleep(random.uniform(1, 4))
            submit.submit()
            sleep(random.uniform(4, 8))
        except:
            if EC.visibility_of_element_located((By.CLASS_NAME, '_ab2z')):
                window['_STLINE_'].update(value="--")
            pass
    auto_chromedriver = chromedriver_autoinstaller.install()

    browser = launch_browser(auto_chromedriver)

    ssl._create_default_https_context = ssl._create_unverified_context
    browser.get('https://www.instagram.com/')
    sleep(3)
    if os.path.exists('Data/' + str(username_str) + '/cookies_file'):
        try:
            LOAD_cookie(browser, username_str)
            pass
        except:
            Login()
    else:
        Login()
    try:
        WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[text()='" + 'Not Now' + "']"))).click()
    except:
        pass
    try:
        WebDriverWait(browser, 4).until(
                EC.visibility_of_element_located((By.XPATH, "//button[text()='" + 'Save Info' + "']"))).click()
    except:
        pass
    SAVE_cookies(browser, username_str, password_str)

    sleep(1)
    likeAndComm(browser)
    sleep(random.uniform(90, 300))

def Bot():
    threading()
    window['_STLINE_'].set_size((WIN_W, 2))
    window['_STLINE_'].expand(expand_x=True, expand_y=True)
    window['_STLINE_'].update("Starting..")
    window['_STLINE_'].update(value="READY..")
    window['_STLINE_'].update(visible=True)
    window['__Next__'].update(visible=False)
    window['__Next__'].Widget.master.pack_forget()
    window['__U__'].update(visible=False)
    window['__U__'].Widget.master.pack_forget()
    window['__USER__'].update(visible=False)
    window['__USER__'].Widget.master.pack_forget()
    window['__P__'].update(visible=False)
    window['__P__'].Widget.master.pack_forget()
    window['__PASS__'].update(visible=False)
    window['__PASS__'].Widget.master.pack_forget()
    window['__H__'].update(visible=False)
    window['__H__'].Widget.master.pack_forget()
    window['__HASH__'].update(visible=False)
    window['__HASH__'].Widget.master.pack_forget()
    window['__COM__'].update(visible=False)
    window['__COM__'].Widget.master.pack_forget()
    window['__C__'].update(visible=False)
    window['__C__'].Widget.master.pack_forget()
    window['__LIK__'].update(visible=False)
    window['__LIK__'].Widget.master.pack_forget()
    window['__L__'].update(visible=False)
    window['__L__'].Widget.master.pack_forget()
    window['__API__'].update(visible=False)
    window['__API__'].Widget.master.pack_forget()
    window['__A__'].update(visible=False)
    window['__A__'].Widget.master.pack_forget()
    window['-HB-'].update(visible=False)
    window['-HB-'].Widget.master.pack_forget()
    window['-HB2-'].update(visible=False)
    window['-HB2-'].Widget.master.pack_forget()
    window['-CB-'].update(visible=False)
    window['-CB-'].Widget.master.pack_forget()
    window['-CB2-'].update(visible=False)
    window['-CB2-'].Widget.master.pack_forget()
    window['-CBT-'].update(visible=False)
    window['-CBT-'].Widget.master.pack_forget()
    window['-CBT2-'].update(visible=False)
    window['-CBT2-'].Widget.master.pack_forget()
    window['_INFO_'].update(value="Loading..")
    window['_STLINE_'].update(value="Starting..")
    sg.SystemTray.notify('BlackGram', 'Bot Starting..')

f=open('Data\settings.txt', 'r')
lines=f.readlines()    
f.close()

x1 = ''.join(re.findall(r'"([^"]*)"', lines[-0]))
x2 = ''.join(re.findall(r'"([^"]*)"', lines[+1]))
x3 = ''.join(re.findall(r'"([^"]*)"', lines[+2]))
x4 = ''.join(re.findall(r'"([^"]*)"', lines[+3]))
x5 = ''.join(re.findall(r'"([^"]*)"', lines[+4]))
x6 = ''.join(re.findall(r'"([^"]*)"', lines[+5]))

window['__USER__'].update(value=x1)
window['__PASS__'].update(value=x2)
window['__HASH__'].update(value=x3)
window['__API__'].update(value=x4)
window['__LIK__'].update(value=x5)
window['__COM__'].update(value=x6)


while True:
    #win32gui.ShowWindow(Minimize,win32con.SW_MINIMIZE)
   
    if __name__ == "__main__":

        event, values = window.read(timeout=100)

        username_str = values['__USER__']
        password_str = values['__PASS__']
        word = values['__HASH__']

        api_key = values['__API__']
            
        openai.api_key = api_key
        
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no(('Do you really want to exit?'), keep_on_top=True) == 'Yes':
            try:
                browser.close()
                browser.quit()
                sys.exit(sys.argv)
            except:
                break
        if event in ('Restart (Ctrl+N)', 'n:78'):
            os.execl(sys.executable, sys.executable, *sys.argv)
        if event == '__Next__':
            Bot()
            try:
                window['C1'].update(value=Rn)
            except:
                pass
        if event == '-CB-':
            window['-HB-'].update(value='Yes', text_color="Lime")
        elif values["-CB-"] == False:
            window['-HB-'].update(value='No', text_color="Red")
        if event == '-CB2-':
            window['-HB2-'].update(value='Yes', text_color="Lime")
        elif values["-CB2-"] == False:
            window['-HB2-'].update(value='No', text_color="Red")
        if event in ('About::-HELP-'):
            webbrowser.open('https://black-bots.github.io/BlackGram.html', new = 2)
        window.refresh()

