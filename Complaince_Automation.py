

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
sleep(10)

#Compliance Admin Application
comp_Admin=Login.find_element(By.XPATH, '//*[@id="allWidgetsTray"]/div[5]/div')
comp_Admin.click()
sleep(5)

#Act Creation
#Country
select_Country = Login.find_element(By.XPATH, '//*[@id="create_act_container"]/div[1]/div/div[1]/div/div/div[2]/ng-select/div/div/div[2]/input')
sleep(5)
select_Country.click()
print("Enter Country: ",end=" ")
select_Country.send_keys(input())
select_Country.send_keys(Keys.ENTER)
sleep(5)

#Act Name
act_Name = Login.find_element(By.XPATH, '//input[@id="actName"]')
sleep(5)
act_Name.click()
print("Enter Act Name: ",end=" ")
act_Name.send_keys(input())
act_Name.send_keys(Keys.ENTER)
sleep(5)

#Act Code
act_Code = Login.find_element(By.XPATH, '//input[@id="actCode"]')
sleep(5)
act_Code.click()
print("Enter Act Code: ",end=" ")
act_Code.send_keys(input())
act_Code.send_keys(Keys.ENTER)
sleep(5)

#Act Version
#Application From
act_Aform = Login.find_element(By.XPATH, '//input[@id="applicableFrom"]')
sleep(5)
act_Aform.click()
aForm_Today=Login.find_element(By.XPATH,'//*[@id="owl-dt-picker-0"]/div[2]/owl-date-time-calendar/div[2]/owl-date-time-month-view/table/tbody/tr[5]/td[2]/span')
sleep(5)
aForm_Today.click()
sleep(5)

#Act Save
act_Save = Login.find_element(By.XPATH, '//*[@id="create_act_container"]/div[1]/div/div[9]/div/button[1]')
sleep(5)
act_Save.click()
sleep(5)

#Act View
act_View=Login.find_element(By.XPATH, '//*[@id="advHomeScroll"]/app-advanced-app/div[1]/div[2]/div/div/div/div/div[2]')
act_View.click()
sleep(5)

#Compliance Creation
comp_Creation=Login.find_element(By.XPATH, '//*[@id="advHomeScroll"]/app-advanced-app/div[1]/div[2]/div/div/div/div/div[3]')
comp_Creation.click()
sleep(5)

#Compliance Country
select_Country = Login.find_element(By.XPATH, '//*[@id="compliance_creation_container"]/div[1]/div/ul/li[1]/div[2]/div[1]/ng-select/div/div/div[2]/input')
sleep(5)
select_Country.click()
print("Enter Country: ",end=" ")
select_Country.send_keys(input())
select_Country.send_keys(Keys.ENTER)
sleep(5)

#Act
act = Login.find_element(By.XPATH, '//*[@id="compliance_creation_container"]/div[1]/div/ul/li[1]/div[2]/div[4]/ng-select/div/div/div[2]/input')
sleep(5)
act.click()
print("Enter Act: ",end=" ")
act.send_keys(input())
act.send_keys(Keys.ENTER)
sleep(5)

#Compliance Code
comp_Code = Login.find_element(By.XPATH, '//*[@id="complianceCode"]')
sleep(5)
comp_Code.click()
print("Enter Act Code: ", end=" ") 
comp_Code.send_keys(input())
comp_Code.send_keys(Keys.ENTER)
sleep(5)

#Compliance Name
comp_Name = Login.find_element(By.XPATH, '//*[@id="complianceName"]')
sleep(5)
comp_Name.click()
print("Enter Act Name: ",end=" ")
comp_Name.send_keys(input())
comp_Name.send_keys(Keys.ENTER)
sleep(5)

#Compliance Date
#Original From
org_Aform = Login.find_element(By.XPATH, '//*[@id="originalApplicableDate"]')
sleep(5)
org_Aform.click()
orgForm_Today=Login.find_element(By.XPATH,'//*[@id="owl-dt-picker-56"]/div[2]/owl-date-time-calendar/div[2]/owl-date-time-month-view/table/tbody/tr[5]/td[2]/span')
orgForm_Today.click()
sleep(5)

#Application From
app_Aform = Login.find_element(By.XPATH, '//*[@id="actApplicableDate"]')
sleep(5)
app_Aform.click()
appForm_Today=Login.find_element(By.XPATH,'//*[@id="owl-dt-picker-57"]/div[2]/owl-date-time-calendar/div[2]/owl-date-time-month-view/table/tbody/tr[5]/td[2]/span')
appForm_Today.click()
sleep(5)

#Compliance Save
comp_Save = Login.find_element(By.XPATH, '//*[@id="compliance_creation_container"]/div[1]/div/div[3]/button[1]')
sleep(5)
comp_Save.click()




