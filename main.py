from selenium import webdriver
import os
directory = os.getcwd()

#Step 0, Preparing the upload function
def recursiveTxtUpload():
    for r, _, f in os.walk(r'articles'):
        for _f in f:
            apath = os.path.join(r, _f)
            _, ext = os.path.splitext(apath)
            if ext == '.txt':
                try:
                    browser.get("http://localhost:8002/wordpress/wp-admin/post-new.php")
                    text_area = browser.find_element_by_css_selector("textarea[id='post-title-0']")
                    with open(apath) as text:
                        words = text.read().split()
                        for word in words:
                         text_area.send_keys(word)
                         text_area.send_keys(" ")
                except Exception as e:
                    print(f'Error while processing {apath} -> {e}')

#Step 1, The setup and the initial number of articles that we want to uplpad
file_count = sum(len(files) for _, _, files in os.walk(r'articles'))
print(file_count)
browser = webdriver.Chrome()

#Step 2, The initial login to Wordpress

browser.get("http://localhost:8002/wordpress/wp-admin/")
username_field = browser.find_element_by_id("user_login")
password_field = browser.find_element_by_id("user_pass")
button_login = browser.find_element_by_css_selector("input[type='submit']")
username_field.send_keys("user")
password_field.send_keys("#CatalinCaldararu#")
button_login.click()

#Step 3, Publishing the articles
directory = 'articles'
recursiveTxtUpload()


