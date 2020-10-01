from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
browser = webdriver.Chrome('./chromedriver')


#CHANGE THIS INTO THE ARRAY , MAYBE MAKE AN ARRAY.PY FILE ThEN IMPORT OK?
#MAKE SURE U HAVE GOOD WIFI
websiteIwanttoCite = 'https://www.forbes.com/billionaires/'


browser.get('https://www.easybib.com')

#THE FUNCTION STARTS HERE
#==============================================================
try:
    citateButton = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/main/div[2]/div/div[1]/a'))
    )
finally:
    citateButton.click()  


websiteChoice = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[1]/section/div/div[2]/div/button[1]')
websiteChoice.click()

time.sleep(1) #wait 1 sec just in case

websiteInput = browser.find_element_by_xpath('//*[@id="search-input"]')
websiteInput.send_keys(websiteIwanttoCite)

searchBtn = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[1]/section/div/div[2]/div/button')
searchBtn.click()
time.sleep(1)

try:
    citeBtn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]/button'))
    )
finally:
    citeBtn.click()               

try:
    cont = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="eval-container1"]/div/div/div/div/a'))
    )
finally:
    cont.click()  

try:
    complete = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="citation_form"]/div[2]/div[2]/button'))
    )                                          
finally:
    complete.click() 

#==============================================================

#IF THIS DOESNT WORK TELL ME, WHEN I TESTED A FEW TIMES IT DIDNT RUN PROPERLY FSR
#at this stage the link is alr citated, 
#in the loop, WHILE the list isn't all citated yet, run the code below. It clicks the 'MAKE ANOTHER CITATION BUTTON':

'''
try:
    citateAgain = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="citation_form"]/div[2]/div[2]/button'))
        XPATH: //*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/button
    )
finally:
    complete.click() 
'''