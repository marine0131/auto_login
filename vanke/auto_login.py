import time
from selenium import webdriver
import pickle
import sys


def login(url, name, passwd):
    # driver = webdriver.Chrome(executable_path='/Users/resolvewang/Documents/program/driver/chromedriver')
    driver = webdriver.Firefox()
    # driver.maximize_window()
    driver.set_window_size(1200,800)

    # process cookies
    # driver.get(url)
    # for k, v in cookies.iteritems():
    #     cookie_dict = {'name': k, 'value': v}
    #     driver.add_cookies(cookie_dict)
    driver.get(url)
    # time.sleep(10)
    curr_url = driver.current_url

    # fill user and passwd
    name_field = driver.find_element_by_id('Telphone')
    name_field.send_keys(name)
    passwd_field = driver.find_element_by_id("Password")
    passwd_field.send_keys(passwd)
    login_button = driver.find_element_by_class_name('btnlogin')

    time.sleep(8)
    login_button.click()

    # cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    # cookiestr = ';'.join(item for item in cookie)
    time.sleep(2)
    pickle.dump(driver.get_cookies(), open('cookies.pkl','wb'))

    driver.close()

    # # get screenshot
    # driver.get_screenshot_as_file('./screenshot.png')

    # # get image
    # element = driver.find_element_by_id('valiCode')
    # left = int(element.location['x'])
    # top = int(element.location['y'])
    # right = int(element.location['x'] + element.size['width'])
    # bottom = int(element.location['y'] + element.size['height'])

    # # process image
    # im = Image.open('screenshot.png')
    # im = im.crop((left,top,right,bottom))
    # im.save('./code.png')
    # # chg_field = driver.find_element_by_class_name('pass-login-tab').find_element_by_class_name('account-title')
    # # chg_field.click()

def process(url):
    driver = webdriver.Firefox()
    driver.set_window_size(1200,800)
    driver.get(url)
    driver.delete_all_cookies()

    # load cookies
    load_cookies(driver, 'cookies.pkl')
    # refresh
    driver.get(url)

    # time.sleep(2.0)
    # if driver.current_url == 'https://fang.vanke.com/Login/OtherUserLogin':
    #     relogin_button = driver.find_element_by_class_name('btn')
    #     relogin_button.click()
    #     time.sleep(3.0)
    #     load_cookies(driver, 'cookies.pkl')
    #     driver.get(url)

    btn_name_list = ['menubar_target', 'menubar_project', 'menubar_wish', 'menubar_product', 'menubar_profile']
    while True:
        for btn_name in btn_name_list:
            btn = driver.find_element_by_id(btn_name)
            btn.click()
            time.sleep(2)

def load_cookies(driver, f):
    try:
        cookies = pickle.load(open(f, 'rb'))
        for cookie in cookies:
            cookie_dict={
                'name': cookie['name'],
                'value': cookie['value'],
                'expires':'',
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False}
            driver.add_cookie(cookie_dict)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    if sys.argv[1] == 'login':
        login_url = "https://fang.vanke.com/"
        login_name = "13656678056"
        login_passwd = "314334wang"
        login(login_url, login_name, login_passwd)
    elif sys.argv[1] == 'loop':
        url = "https://fang.vanke.com/"
        process(url)
    else:
        pass
