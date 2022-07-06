from pydoc import classname
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

print("Please enter the class number you want to check the availability for: ")
classUserWants = input()

driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
website = "https://webapp4.asu.edu/catalog/"
driver.get(website)

keyword = driver.find_element(By.ID,"keyword")
keyword.send_keys(classUserWants)
driver.find_element(By.ID,"searchTypeAllClass").click()
driver.find_element(By.ID,"go_and_search").click()
driver.implicitly_wait(15)
seatsOpen = driver.find_element(By.XPATH,'//*[@id="informal"]/td[11]/div/span[1]').text

if(int(seatsOpen) > 0):
    print("There are " + seatsOpen + "for the class #" + classUserWants)
else:
    print("There are no available seats for the class #" + classUserWants)


#78128
