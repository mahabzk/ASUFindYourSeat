from pydoc import classname
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import keys
from twilio.rest import Client

client = Client(keys.account_sid,keys.auth_token)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='./drivers/chromedriver' , options=options)

print("Please enter the class number you want to check the availability for: ")
classUserWants = input()
print("Please enter the number to send a message for updates?")
usersPhoneNumber = input()

website = "https://webapp4.asu.edu/catalog/"
driver.get(website)

keyword = driver.find_element(By.ID,"keyword")
keyword.send_keys(classUserWants)
driver.find_element(By.ID,"searchTypeAllClass").click()
driver.find_element(By.ID,"go_and_search").click()
driver.implicitly_wait(15)
seatsOpen = driver.find_element(By.XPATH,'//*[@id="informal"]/td[11]/div/span[1]').text

def classIsOpen():
    message = client.messages.create(
        body="The class #" + classUserWants + " is open",
        from_= keys.twilio_number,
        to= usersPhoneNumber
    )

if(int(seatsOpen) > 0):
    classIsOpen()
else:
    while(seatsOpen == 0):
        sleep(300)
        driver.refresh()
        seatsOpen = driver.find_element(By.XPATH,'//*[@id="informal"]/td[11]/div/span[1]').text
    classIsOpen()
       
driver.close()



#78128
