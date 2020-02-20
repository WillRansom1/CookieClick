import os , time , keyboard
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

# Using Chrome to access web
driver = webdriver.Chrome(r"C:\Users\William Ransom\Desktop\New folder\chromedriver.exe")
# Open the website
driver.set_page_load_timeout('10')
driver.get('https://orteil.dashnet.org/cookieclicker/')
cookies = 0
#set options real quick short numbers off
#5 seconds to change options
time.sleep(20)
cursorButton = driver.find_element_by_id('product0')
gmaButton = driver.find_element_by_id('product1')
fmButton = driver.find_element_by_id('product2')
minButton = driver.find_element_by_id('product3')
ftButton = driver.find_element_by_id('product4')
bkButton = driver.find_element_by_id('product5')
tempButton = driver.find_element_by_id('product6')
wtButton = driver.find_element_by_id('product7')
stButton = driver.find_element_by_id('product8')
alButton = driver.find_element_by_id('product9')
portButton = driver.find_element_by_id('product10')
timeButton = driver.find_element_by_id('product11')
antiButton = driver.find_element_by_id('product12')
prismButton = driver.find_element_by_id('product13')
chancButton = driver.find_element_by_id('product14')
feButton = driver.find_element_by_id('product15')
jsButton = driver.find_element_by_id('product16')
cookie =  driver.find_element_by_id('bigCookie')
# Cookie Code
cookiesRaw = driver.find_element_by_xpath('//*[@id="cookies"]')
#cookies = cookiesRaw.get_attribute('cookies.title')
while True:
    cookiesStr = cookiesRaw.get_attribute('textContent').replace(',','')
    cookiesArr = [int(i) for i in cookiesStr.split() if i.isdigit()]
    cookies = int(cookiesArr[0]) 
    cursorPrice = int((driver.find_element_by_id('productPrice0')).get_attribute('textContent').replace(',',''))
    gmaPrice = int((driver.find_element_by_id('productPrice1')).get_attribute('textContent').replace(',',''))
    fmPrice = int((driver.find_element_by_id('productPrice2')).get_attribute('textContent').replace(',',''))
    minPrice = int((driver.find_element_by_id('productPrice3')).get_attribute('textContent').replace(',',''))
    ftPrice = int((driver.find_element_by_id('productPrice4')).get_attribute('textContent').replace(',',''))
    bkPrice = int((driver.find_element_by_id('productPrice5')).get_attribute('textContent').replace(',',''))
    tempPrice = int((driver.find_element_by_id('productPrice6')).get_attribute('textContent').replace(',',''))
    wtPrice = int((driver.find_element_by_id('productPrice7')).get_attribute('textContent').replace(',',''))
    stPrice = int((driver.find_element_by_id('productPrice8')).get_attribute('textContent').replace(',',''))
    alPrice = int((driver.find_element_by_id('productPrice9')).get_attribute('textContent').replace(',',''))
    portPrice = int((driver.find_element_by_id('productPrice10')).get_attribute('textContent').replace(',',''))
    timePrice = int((driver.find_element_by_id('productPrice11')).get_attribute('textContent').replace(',',''))
    antiPrice = int((driver.find_element_by_id('productPrice12')).get_attribute('textContent').replace(',',''))
    prismPrice = int((driver.find_element_by_id('productPrice13')).get_attribute('textContent').replace(',',''))
    chancPrice = int((driver.find_element_by_id('productPrice14')).get_attribute('textContent').replace(',',''))
    fePrice = int((driver.find_element_by_id('productPrice15')).get_attribute('textContent').replace(',',''))
    jsPrice = int((driver.find_element_by_id('productPrice16')).get_attribute('textContent').replace(',',''))
#    print(cookies)
    cookie.click()
    time.sleep(0.00001)
    try: 
        upgradeCl = driver.find_element_by_class_name('crate upgrade enabled')
    except NoSuchElementException:
        upgradeCl = 'null'
    if upgradeCl == 'crate upgrade enabled':
        upgradeCl.click
    if cookies >= jsPrice:
        jsButton.click()
    elif cookies >= fePrice:
        feButton.click()
    elif cookies >= chancPrice:
        chancButton.click()
    elif cookies >= prismPrice:
        prismButton.click()
    elif cookies >= antiPrice:
        antiButton.click()
    elif cookies >= timePrice:
        timeButton.click()
    elif cookies >= portPrice:
        portButton.click()
    elif cookies >= alPrice:
        alButton.click()
    elif cookies >= stPrice:
        stButton.click()
    elif cookies >= wtPrice:
        wtButton.click()
    elif cookies >= tempPrice:
        tempButton.click()
    elif cookies >= bkPrice:
        bkButton.click()
    elif cookies >= ftPrice:
        ftButton.click()
    elif cookies >= minPrice:
        minButton.click()
    elif cookies >= fmPrice:
        fmButton.click()
    elif cookies >= gmaPrice:
        gmaButton.click()
    elif cookies > cursorPrice:
        cursorButton.click()
    