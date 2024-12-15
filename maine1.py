from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')

user_message = driver.find_element(By.ID, "user-message")
user_message.send_keys("name")


login_button = driver.find_element(By.ID,"showInput")
login_button.click()
sleep(5)