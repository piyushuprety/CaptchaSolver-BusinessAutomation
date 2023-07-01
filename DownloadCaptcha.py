from selenium.webdriver.common.keys import Keys
import time


def audio(act):

    time.sleep(1)
    for i in range(4):
        act.send_keys(Keys.TAB).perform()
        act.send_keys(Keys.SPACE).perform()
    act.send_keys(Keys.TAB).perform()
    act.send_keys(Keys.ENTER).perform()
    act.send_keys(Keys.ARROW_UP).perform()
    act.send_keys(Keys.ENTER).perform()
    a='C://Users/Piyush/Downloads/audiocaptcha.mp3'
    return (a)
