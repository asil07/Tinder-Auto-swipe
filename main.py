from selenium import webdriver
from selenium.common.exceptions import *
import time
EMAIL = "your email"
PASSWORD = "Your password"
CHROME_PATH = "your driver path"

chrome_path = "C:/development/chromedriver.exe"
edge_path = "C:/development/msedgedriver.exe"
driver = webdriver.Chrome(CHROME_PATH)

driver.get("https://tinder.com/")
login = driver.find_element_by_css_selector(".button")
login.click()

time.sleep(2)
via_fb = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
via_fb.click()


base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_id("email")
email.send_keys(EMAIL)
password = driver.find_element_by_id("pass")
password.send_keys(PASSWORD)
login = driver.find_element_by_name("login")
login.click()
time.sleep(5)
# confirm = driver.find_element_by_name("__CONFIRM__")
# confirm.click()
# yangiliklar boladi

driver.switch_to.window(base_window)

time.sleep(5)
allow_location = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(3)
notification_disable = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div/div/div[3]/button[2]')
notification_disable.click()
time.sleep(3)
accept_terms = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[2]/div/div/div[1]/button')
accept_terms.click()
time.sleep(3)
game_is = True
while game_is:
    try:
        like_button = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()
        time.sleep(2)
    except NoSuchElementException:
        pass
    except ElementClickInterceptedException:
        try:
            add_tinder_home_disable = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[2]/button[2]')
            add_tinder_home_disable.click()
            time.sleep(2)
        except NoSuchElementException:
            try:
                match_popup = driver.find_element_by_xpath('//*[@id="t-1991125185"]/div/div/div[1]/div/div[4]/button')
                match_popup.click()
                time.sleep(2)
            except NoSuchElementException:
                super_like = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/button[1]')
                super_like.click()
                time.sleep(15)








