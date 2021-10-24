import os
from datetime import time

from selenium.webdriver.common.keys import Keys

directory = os.getcwd()

def recursiveArticleUpload(browser):
    for r, _, f in os.walk(r'articles'):
        for _f in f:
            apath = os.path.join(r, _f)
            _, ext = os.path.splitext(apath)
            if ext == '.txt':
                #check for the alert and treat it separate
                try:
                    browser.get("http://localhost:8002/wordpress/wp-admin/post-new.php")
                    text_area = browser.find_element_by_css_selector("textarea[id='post-title-0']")
                    with open(apath) as text:
                        words = text.read().split()
                        for word in words:
                         text_area.send_keys(word)
                         text_area.send_keys(" ")
                    time.sleep(15)
                    browser.find_element_by_xpath("//button[text()='Publish']").click()
                    browser.sendKeys(Keys.CONTROL + "S")
                    time.sleep(15)
                    browser.find_element_by_css_selector('button.components-button.editor-post-publish-button.editor-post-publish-button__button.is-primary').click()
                except Exception as e:
                    print(f'Error while processing {apath} -> {e}')