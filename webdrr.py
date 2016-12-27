from selenium import webdriver
import time
from random import randint
import datetime

#f = webdriver.Chrome()
#f.get('http://di.fm')
#print (f.title)
##f.save_screenshot('d:/123.jpg')
#link = f.find_element_by_xpath("id('login-signup')/ul/li[2]/a")
#link.click()
##link.click()
#field = f.find_element_by_id('member_email')
#field.send_keys('m3quattro@mail.ru')
#field = f.find_element_by_id('member_password')
#field.send_keys('erhehetherh')
#field = f.find_element_by_id('member_password_confirmation')
#field.send_keys('erhehetherh')
#field.submit()

f_email = webdriver.Chrome()
time.sleep(2)
f_email.get('https://10minutemail.net/?lang=ru')
time.sleep(2)
f_registration  = webdriver.Chrome()
time.sleep(2)
f_registration.get('https://sprk.sphero.com/account/sign_up/instructor')

password = 'qwerty123'
path_log = r'd:\syslog.txt'

def get_addr_email():
    pochta = f_email.find_element_by_id('fe_text')
    pochta = pochta.get_attribute('value')
    return pochta

def login_generator():
    symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_0123456789qazQAZ2wsxWSX3edcEDC4rfvRFV5tgbTGB6yhnYHN7ujmUJM8ikIK9plPL_0'
    login=[]
    lenght_login = randint(6,12)
    for i in range(0, lenght_login):
        login.append(symbols[randint(0, len(symbols))])
        return''.join(login)

def write_log(message):
    f = open(path_log, 'a')
    f.write('{0} {1}\n'.format(message, datetime.datetime.now()))
    f.close()

def reg_step1():
    xpath_login = "id('app')/div/div[2]/div/div/div/div[1]/input"
    xpath_email = "id('app')/div/div[2]/div/div/div/div[2]/input"
    xpath_pass = "id('app')/div/div[2]/div/div/div/div[3]/input"
    xpath_pass_v = "id('app')/div/div[2]/div/div/div/div[4]/input"
    xpath_button = "id('app')/div/div[2]/div/div/div/button"
    email = get_addr_email()
    login = login_generator()
    field = f_registration.find_element_by_xpath(xpath_login)
    field.send_keys(login)
    field = f_registration.find_element_by_xpath(xpath_email)
    field.send_keys(email)
    field = f_registration.find_element_by_xpath(xpath_pass)
    field.send_keys(password)
    field = f_registration.find_element_by_xpath(xpath_pass_v)
    field.send_keys(password)
    field = f_registration.find_element_by_id(xpath_button)
    field.click()
    write_log(login)
reg_step1()