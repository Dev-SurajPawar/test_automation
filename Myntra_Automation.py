

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


browser=webdriver.Chrome(executable_path="/home/suraj/Desktop/chromedriver")
browser.get("https://myntra.com")

sleep(10)

search_box = browser.find_element(By.CLASS_NAME, 'desktop-searchBar')

sleep(5)

search_box.click()

sleep(5)

print("What you want to search: ",end=" ")
search_box.send_keys(input())
search_box.send_keys(Keys.ENTER)


