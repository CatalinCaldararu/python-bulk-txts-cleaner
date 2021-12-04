from selenium import webdriver
from Utils.wordpressLogin import loginToWordPress

browser = webdriver.Chrome()
loginToWordPress(browser)
