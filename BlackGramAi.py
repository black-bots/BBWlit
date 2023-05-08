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
import streamlit as st
import sys
import openai
import prompt_toolkit
import os
import pickle
import shutil
import ssl
import re

model=""

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
    
checkedd = True


def rsleep(self, minimum=1, maximum=5):
    t = randint(minimum, maximum)

    for remaining in range(5, 0, -1):
        st.write(value="        Waiting {:2d} seconds -\n".format(remaining))
        sleep(1)
    sleep(t)

def threading():
    t = Thread(target=start, daemon=True)
    t.start()

posts=0
commentss=0
follows = 0

def start():
    st.write('Likes: ')
    st.write(str(posts))
    st.write(str(commentss))
    st.write(str(follows))
  
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
        st.write("Comment +1")
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
        st.write("Deciding to Like or not..")                    
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
                        st.write("Post Liked")
                        sleep(random.uniform(2, 4))
                    else:
                        sleep(random.uniform(2, 4))
                except:
                    likeAndComm(browser)
            else:
                next(browser)
            st.write("Trying to Comment..")
            sleep(random.uniform(2, 6))
            chance = random.randint(1,100)
            if chance <= int(x6):
                try:
                    Comment(browser)
                    st.write("Post Commented")
                    commentss +=1

                except:
                    likeAndComm(browser)
            if chance <= int(x6):
                if values["-CB2-"] == True:
                    st.write("Trying to Follow..")
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

            st.write("Waiting..")
            watin = sleep(random.uniform(10, 60))

            st.write("Loading..")
            st.write('Likes: ')
            st.write(str(posts))
            st.write('Comments: ')
            st.write(str(commentss))
            st.write('Follows: ')
            st.write(str(follows))
            next(browser)
        if postss >= 10:
            closePost=  WebDriverWait(browser, 10).until(
                            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div')))
            closePost.click()
            postss = 0
        else:
            next(browser)
        st.write(ZZ + ' Zzz')
        st.write('Sleeping..: ')
        st.write('Likes: ')
        st.write(str(posts))
        st.write('Comments: ')
        st.write(str(commentss))
        st.write('Follows: ')
        st.write(str(follows))

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

            if checkedd == True:
                 chrome_options.add_argument("--headless")
                 chrome_options.add_argument("window-size=1000,700")
                 user_agent = "Chrome"
                 chrome_options.add_argument('user-agent={user_agent}'
                                             .format(user_agent=user_agent))
                 st.write("Botting behind the scenes(Chrome)")
            browser = webdriver.Chrome(path_to_chromedriver, options=chrome_options)
            st.write("Chrome Browser Selected")

        except:
            try:
                webdriver.quit()
                pass
            except:
                pass
            st.write("Chrome not detected. Trying Firefox..")
            get_geckodriver()
            sleep(4)
            firefox_options = Firefox_Options()
            browser = webdriver.Firefox(executable_path="geckodriver.exe", options=firefox_options)
            st.write("Firefox Browser Selected")
            if checkedd == True:
                 firefox_options.add_argument("--headless")
                 firefox_options.add_argument("window-size=1000,700")
                 user_agent = "Firefox"
                 chrome_options.add_argument('user-agent={user_agent}'
                                             .format(user_agent=user_agent))
                 st.write("Botting behind the scenes(Firefox)")
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
            st.write("Instagram.com")
            sleep(3)
            st.write("Trying Cookie..")
            load_cookie(browser, username_str)
            browser.get('https://www.instagram.com/' + username_str)
            st.write(username_str)
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
            st.write("Logging In..")
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
                st.write("--")
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
    st.write("Starting..")
    st.write("READY..")
    st.write("Loading..")
    st.write("Starting..")

f=open('Data\settings.txt', 'r')
lines=f.readlines()    
f.close()


while True:
   
    if __name__ == "__main__":
        ok = st.button('Start')
        event, values = window.read(timeout=100)

        username_str = 	st.text_input("Username","username",help="Enter your Instagram Username")
        password_str = st.text_input("Password","pass123",type="password",help="Enter your Instagram Password")
        word = st.text_input("#Tag","movies",help="Enter your Focus Word")

        api_key = st.text_input("api-key","sk-2J9D32BD8QN32",type="password",help="Enter your OpenAi Api-Key")
            
        openai.api_key = api_key
        

        if ok:
            Bot()
            try:
                st.write(Rn)
            except:
                pass

        window.refresh()

