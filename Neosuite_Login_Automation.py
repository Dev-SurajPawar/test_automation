

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#Login page
Login=webdriver.Chrome(executable_path="/home/suraj/Desktop/chromedriver")
Login.get("https://neosuiteuat.neeyamo.works")
Login.maximize_window()
sleep(10)

#Employee ID 
search_employeeID = Login.find_element(By.XPATH, '//input[@id="username"]')

sleep(5)

search_employeeID.click()
print("Enter Employee ID: ",end=" ")
search_employeeID.send_keys(input())

#Password
search_password = Login.find_element(By.XPATH, '//input[@id="password"]')

sleep(5)

search_password.click()
print("Enter Password: ",end=" ")
search_password.send_keys(input())

#Login Click
search_login = Login.find_element(By.XPATH, '//input[@id="kc-login"]')

search_login.click()

