from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def read():
    s = Service("D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://speech-to-text-demo.ng.bluemix.net/")
    act = ActionChains(driver)
    for i in range(16):
        act.send_keys(Keys.TAB).perform()
    time.sleep(2)
    location = 'C://Users/Piyush/Downloads/audiocaptcha.mp3'
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    element.send_keys(location)
    time.sleep(6)
    for element in driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span'):
        cap = element.text
    captcha = cap[:6]
    return (captcha)

