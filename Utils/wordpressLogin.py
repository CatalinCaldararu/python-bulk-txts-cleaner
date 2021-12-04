def loginToWordPress(browser):
    browser.get("http://localhost:8002/wordpress/wp-admin/")
    username_field = browser.find_element_by_id("user_login")
    password_field = browser.find_element_by_id("user_pass")
    button_login = browser.find_element_by_css_selector("input[type='submit']")
    username_field.send_keys("user")
    password_field.send_keys("#CatalinCaldararu#")
    button_login.click()
