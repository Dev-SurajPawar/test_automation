

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
sleep(5)

#Vendor Application
Vendor=Login.find_element(By.XPATH, '//*[@id="allWidgetsTray"]/div[7]/div')
Vendor.click()
sleep(5)

#Create Vendor
Create=Login.find_element(By.XPATH, '//*[@id="vendorMaster_vendors_ListViewaddIconsChild8"]')
Create.click()
sleep(5)

#Add Vendor Name
VndName=Login.find_element(By.XPATH, '//*[@id="vendorName"]')
print("Enter Vendor Name: ",end=" ")
VndName.send_keys(input())
sleep(5)

#Add Vendor Code
VndCode=Login.find_element(By.XPATH,'//*[@id="vendorCode"]')
print("Enter Vendor Code: ",end=" ")
VndCode.send_keys(input())
sleep(5)


#Vendor Department
VndDepartment=Login.find_element(By.XPATH,'//*[@id="departmentCode"]/div/div/div[2]/input')
sleep(5)
VndDepartment.click()
print("Enter Department: ",end=" ")
VndDepartment.send_keys(input())
VndDepartment.send_keys(Keys.ENTER)
sleep(5)

#Vendor Status
VndStatus=Login.find_element(By.XPATH,'//*[@id="vendorStatus"]/div/div/div[2]/input')
sleep(5)
VndStatus.click()
print("Enter Vendor Status: ",end=" ")
VndStatus.send_keys(input())
VndStatus.send_keys(Keys.ENTER)
sleep(10)


#Vendor Country
VndCountry=Login.find_element(By.XPATH,'//*[@id="countryCode"]/div/div/div[2]/input')
sleep(5)
VndCountry.click()
print("Enter Vendor Country: ",end=" ")
VndCountry.send_keys(input())
VndCountry.send_keys(Keys.ENTER)
sleep(5)


#Sign Date
VndSignDate=Login.find_element(By.XPATH,'//*[@id="contractSignedDate"]')
VndSignDate.click()
sleep(5)
VndSignDateToday=Login.find_element(By.XPATH,'//*[@id="owl-dt-picker-1"]/div[2]/owl-date-time-calendar/div[2]/owl-date-time-month-view/table/tbody/tr[4]/td[7]')
VndSignDateToday.click()
sleep(5)
SignDateSet=Login.find_element(By.XPATH,'//*[@id="owl-dt-picker-1"]/div[2]/div/button[2]/span')
SignDateSet.click()
sleep(5)

#END Date
VndEndDate=Login.find_element(By.XPATH,'//*[@id="contractEndDate"]')
VndEndDate.click()
sleep(5)
VndEndDateToday=Login.find_element(By.XPATH,'//*[@id="owl-dt-picker-2"]/div[2]/owl-date-time-calendar/div[2]/owl-date-time-month-view/table/tbody/tr[4]/td[7]')
VndEndDateToday.click()
sleep(5)
SignEndSet=Login.find_element(By.XPATH,'//*[@id="owl-dt-picker-2"]/div[2]/div/button[2]/span')
SignEndSet.click()
sleep(10)

#Save
VndSave=Login.find_element(By.XPATH,'//*[@id="vendor_master_create_view"]/div[2]/div[14]/div/button')
VndSave.click()


