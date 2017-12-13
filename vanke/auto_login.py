import time
from selenium import webdriver
import pickle
import sys
import re

def login(url, name, passwd):
    driver = webdriver.Chrome(executable_path='C:\Python27\chromedriver')
    # driver = webdriver.Firefox()
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

# >>>>>>>>>>>look from here
def process(url):
    # open chrome or firefox, set windows size, clear cookies
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome(executable_path='C:\Python27\chromedriver')
    driver.set_window_size(1200,800)
    driver.get(url)
    driver.delete_all_cookies()
    
    # load cookies
    load_cookies(driver, 'cookies.pkl')
    
    # refresh
    driver.get(url)

    # into the specified building website
    url = "https://fang.vanke.com/ActivityTarget/Floor/58340?activityid=12418"
    driver.get(url)

    # click blank space
    driver.find_element_by_class_name('modal-backdrop').click()
    # driver.find_element_by_xpath("//img[@src='/Content/images/bottom_logo.png']").click()
    time.sleep(2.0)

    # find the excat room id
    link = driver.find_element_by_xpath('//a[@data-href="/ActivityTarget/Auction?id=2740154"]')

    # while loop
    while True:
        # if time reach the exact time
        # if time.time() > 1513072920.000:  # 
        if time.time() > 1513076400.000:   # 12/12 19:00
            # click the link
            link.click()
            try:
                driver.find_element_by_class_name(r"add_price*").click()
                print time.time()
            except Exception:
                print("can not find button")
            break
        
    # loop forever and print time
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        time.sleep(1.0)


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
