
# coding: utf-8

# In[1]:

import pyautogui as pya
from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://10fastfingers.com/typing-test/english")
window = driver.current_window_handle
driver.switch_to.window(window)


test = driver.find_element_by_id("wordlist")
wordlist = test.get_attribute("textContent")
wordlist = wordlist.replace("|", " ")

time.sleep(10)
pya.typewrite(wordlist, interval=0.03)
pya.press(" ")

