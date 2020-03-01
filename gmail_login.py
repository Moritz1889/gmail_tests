import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import pyautogui as pg

def tap_string_on_keyboard(string):
    actions = ActionChains(driver)
    actions.send_keys(string)
    actions.perform()

def run_gmail_login():
    global driver

    ## Chrome Driver ##
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    url = "https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    driver.get(url)
    print("Display and driver started")
    wait = WebDriverWait(driver,50)
    time.sleep(5)

    # Entering an email
    wait.until(lambda driver: driver.find_element_by_id('identifierId'))
    email_input = driver.find_element_by_id('identifierId')
    email_input.click()
    tap_string_on_keyboard('janusz.biznesu85@gmail.com')

    wait.until(lambda driver: driver.find_element_by_id('identifierNext'))
    next_button_email = driver.find_element_by_id('identifierNext')
    next_button_email.click()
  
    # Entering a password
    wait.until(lambda driver: driver.find_element_by_id('password'))
    password_input = driver.find_element_by_id('password')
    password_input.click()
    tap_string_on_keyboard('teamplay')

    wait.until(lambda driver: driver.find_element_by_id('passwordNext'))
    next_button_passowrd = driver.find_element_by_id('passwordNext')
    next_button_passowrd.click()

def run():
    successful_test = 0
    while successful_test<1:
        print("Running")
        run_gmail_login()
        successful_test+=1

if __name__ == "__main__":
    run()