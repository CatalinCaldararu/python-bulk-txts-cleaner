from selenium import webdriver
from articleUpload import recursiveArticleUpload
from wordpressLogin import loginToWordPress

browser = webdriver.Chrome()
loginToWordPress(browser)
recursiveArticleUpload(browser)


