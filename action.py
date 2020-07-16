#!/usr/bin/python
#filename    : action
#aurthor     : ashish varshney

from library import *

def action(username_entry, url_entry):
    username = username_entry.get() # get name from Entry widget
    url = url_entry.get() # get url from Entry widget

    while True:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        driver.get(url)
        namebox = driver.find_element_by_id("v")
        namebox.send_keys(username)
        submit = driver.find_element_by_id("vote_btn")
        submit.click()
        time.sleep(30)
        driver.quit()
        time.sleep(1800)
