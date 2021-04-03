print (
'''
----------------------------------------------------------------------
Created By :: Thamizhan_PS

Github_ID :: https://github.com/thamizhanps/

Contact Me : psthamizhan01@gmail.com
----------------------------------------------------------------------
''')

#Import Files
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform

print ('*** Note :: File Names must as .txt (Eg : abcd.txt) *** \n')

#Get Inputs
country = input("Enter Country Code :: ")
msg = input("Enter Message File Name :: ")
cnt = input("Enter Contact File Name :: ")

#Start Grabbing
f= open(msg , "r", encoding='utf-8', errors='ignore')
message = f.read()
f.close()

message = quote(message)

numbers = []
f = open(cnt, "r")
for line in f.read().splitlines():
    if line != "":
        numbers.append(line)
f.close()

total_number=len(numbers)

#Start Process
print("\n--------------------------------------------------------------")
print('We found ' + str(total_number) + ' numbers in the file')
print("--------------------------------------------------------------")

delay = 30

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./BWS')

driver = webdriver.Chrome("chromedriver.exe" , options = options)

driver.get('https://web.whatsapp.com')

input("\nPress ENTER after login into Whatsapp Web and your chats are visiable....")

for idx, number in enumerate(numbers):
    if number == "":
        continue
    print('{}/{} => Sending message to ::  {}.'.format((idx+1), total_number, number))
    try:
        driver.get("https://web.whatsapp.com/send?phone="+country+number+"&text="+message)
        sleep(7)
        click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME , '_1E0Oz')))
        sleep(2)
        click_btn.click()
        sleep(3)
        print("Message Sent To :: " + number)

    except Exception as e:
        print("---------------------------------------------------------------------------")
        print('\nFailed to send message to ' + number + str(e))
        print("---------------------------------------------------------------------------")


#Quit Driver
driver.quit()
