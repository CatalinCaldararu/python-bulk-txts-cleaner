from selenium import webdriver
import os
directory = os.getcwd()

#Open the Chrome Instance
browser = webdriver.Chrome()

#Loop --> Iterate through the txt files and publish them to wordpress
#Step 1 Connect To Wordpress
browser.get("http://localhost:8002/wordpress/wp-admin/post-new.php")
username_field = browser.find_element_by_id("user_login")
password_field = browser.find_element_by_id("user_pass")
button_login = browser.find_element_by_css_selector("input[type='submit']")

#Step 2 Login to WordPress
username_field.send_keys("user")
password_field.send_keys("#CatalinCaldararu#")
button_login.click()

#Step 3 Define your TXT contents
hello_variable = "Hello world"

#Step 4 Copy your TXT contents to the textarea
text_area = browser.find_element_by_css_selector("textarea[id='post-title-0']")
text_area.send_keys(hello_variable)

#Step 5 Press the publish button

#Repeat Until Completed