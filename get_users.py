from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from lxml import html
import pandas as pd
from bs4 import BeautifulSoup


username='User_name'#your username
password='password'#your password
site='https://www.facebook.com'

browser = webdriver.Chrome("chromedriver.exe")

# Email and password elements
username_xpath = "//input[@id='email']"
password_xpath = "//input[@id='pass']"
login_button_xpath = '//*[@id="loginbutton"]'

browser.get(site)

username_element = browser.find_element_by_xpath(username_xpath)
password_element = browser.find_element_by_xpath(password_xpath)

# Writing the username and password
username_element.send_keys(username)
password_element.send_keys(password)


# Logging in
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginbutton"]'))).click()


body =browser.find_element_by_tag_name('body')
for i in range(1):
    body.send_keys(Keys.ESCAPE)

liste=[]
#browsing the page
browser.get("")#post link (replace www.facebook.com/ to m.facebook.com/ )
body = browser.find_element_by_tag_name('body')
for i in range(10):
    body.send_keys(Keys.ESCAPE)
for i in range(1000):
    body.send_keys(Keys.END)
    browser.implicitly_wait(1)
    try:
        


        
        
        linke=browser.find_element_by_xpath('//*[@id="reaction_profile_pager"]/a')
        linke.click()
    except:
        pass


profile_soup = BeautifulSoup(browser.page_source, 'lxml')
ms=profile_soup.find_all('div', attrs={'_1uja'})

for x in range(len(ms)):
    r=ms[x].findAll('a',attrs={'class': 'darkTouch _1aj5 l'})
    try:
        for xx in range(len(r)):
            liste.append(r[xx]['href'])
    except:
        pass




    

new=[]

for i in range(len(liste)):
        if liste[i][13:15]=='id':
            x1=liste[i].find('id')
            x1=x1+3
            y1=liste[i].find('&fref')
            st=liste[i][x1:y1]
            if st not in new: 
                new.append(st)

        elif '?fref' in liste[i]:
            x2=1
            y2=liste[i].find('?fref')
            st1=liste[i][x2:y2]
            if st1 not in new:
                new.append(st1)
            




with open("friends_data.txt",'a') as F:
	for i in range(len(new)):
		F.write('\n'+new[i])
	F.close()
