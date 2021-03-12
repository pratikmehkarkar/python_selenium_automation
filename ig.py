from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from getpass import getpass
from links import my_website
from links import PATH
driver = webdriver.Chrome(PATH)


#------------------------------------------------------------------------------------------------------------------------------------------
def log_in_to_instagram(driver,website):
    driver.get(website)
    username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear() #used to clear out default txt on username box
    ig_username = input('Enter your instagram username: ')
    username.send_keys(ig_username)
    password.clear()
    ig_pass = getpass('enter your instagram password: ')
    password.send_keys(ig_pass)
    login_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
    not_now_notifications = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
#------------------------------------------------------------------------------------------------------------------------------------------
def search_profile(driver):
    searchbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    keyword = input("enter what you want to search: ")
    searchbox.send_keys(keyword)
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(1)
    searchbox.send_keys(Keys.ENTER)
    ans = input('do you want to follow this account? : (Y or N) ')
    if (ans == 'Y' or ans == 'y'):
        follow_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Follow')]"))).click()
    else:
        print('going back to main menu')
        go_to_main_Menu(driver)
#------------------------------------------------------------------------------------------------------------------------------------------
def go_to_main_Menu(driver):
    main_menu = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[class='s4Iyt']"))).click()

#------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    log_in_to_instagram(driver,my_website)
    answer = input('do you want to search for a instagram profile? (Y or N) ')
    if (answer == 'Y' or answer == 'y'):
        search_profile(driver)
    else:
        go_to_main_Menu(driver)
