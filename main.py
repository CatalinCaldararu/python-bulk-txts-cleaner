import options as options
from selenium import webdriver
from articleUpload import recursiveArticleUpload
from wordpressLogin import loginToWordPress

options = webdriver.ChromeOptions()
options.add_argument(r'--disable-popup-blocking')
browser=webdriver.Chrome(chrome_options=options, executable_path=r"C:/Users/HP/projects/drivers/chromedriver.exe")

#browser = webdriver.Chrome()
loginToWordPress(browser)
recursiveArticleUpload(browser)
