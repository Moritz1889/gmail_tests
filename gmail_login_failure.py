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

def run_gmail_login_failure():
    global driver 

    ## Chrome Driver ##
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    url = "https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    driver.get(url)
    print("Display and driver started")
    wait = WebDriverWait(driver,50)
    time.sleep(5)

    # Entering a wrong email

    wait.until(lambda driver: driver.find_element_by_id('identifierId'))
    email_input = driver.find_element_by_id('identifierId')
    email_input.click()
    tap_string_on_keyboard('janusz.biznesu85@gmail.comm')

    wait.until(lambda driver: driver.find_element_by_id('identifierNext'))
    next_button_email = driver.find_element_by_id('identifierNext')
    next_button_email.click()

    wait.until(lambda driver: driver.find_element_by_xpath("//*[contains(text(), 'Nie pamiętasz adresu?')]"))
    message_error = driver.find_element_by_xpath("//*[contains(text(), 'Nie pamiętasz adresu?')]")

    if message_error.is_displayed():
        print("Error message found")
    else:
        print("Error message did not found")

def run():
    successful_test = 0
    while successful_test<1:
        print("Running")
        run_gmail_login_failure()
        successful_test+=1

if __name__ == "__main__":
    run()