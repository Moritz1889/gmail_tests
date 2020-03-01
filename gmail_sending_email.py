# Because of recent changes made by Google, Google does not allow log in via automated tests. So, the begining of the test works, but not the sending mail part. 

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

def tap_string_on_keyboard(string):
    actions = ActionChains(driver)
    actions.send_keys(string)
    actions.perform()

def run_sending_email():
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

    # Creating an email
    wait.until(lambda driver: driver.find_element_by_id('T-I J-J5-Ji T-I-KE L3'))
    button_create = driver.find_element_by_class_name('T-I J-J5-Ji T-I-KE L3')
    button_create.click()

    # Entering Receiver email
    wait.until(lambda driver: driver.find_element_by_id(':10y'))
    receiver_input = driver.find_element_by_id(':10y')
    receiver_input.click()
    tap_string_on_keyboard('b.babirecki@gmail.com')

    # Entering subject
    wait.until(lambda driver: driver.find_element_by_id(':10g'))
    subject_input = driver.find_element_by_id(':10g')
    subject_input.click()
    tap_string_on_keyboard('Test mail')

    # Entering content
    wait.until(lambda driver: driver.find_element_by_id(':11l'))
    content_input = driver.find_element_by_id(':11l')
    content_input.click()
    tap_string_on_keyboard('Hello, this is a test mail')

    # Sending the email
    wait.until(lambda driver: driver.find_element_by_id(':106'))
    button_send = driver.find_element_by_id(':106')
    button_send.click()
    time.sleep(5)

def run():
    successful_test = 0
    while successful_test<1:
        print("Running")
        run_sending_email()
        successful_test+=1

if __name__ == "__main__":
    run()