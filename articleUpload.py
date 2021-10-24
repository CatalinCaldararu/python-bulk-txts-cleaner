import os
directory = os.getcwd()

def recursiveArticleUpload(browser):
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