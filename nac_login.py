  GNU nano 5.4                                                                                          nac.py
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

options = FirefoxOptions()
options.add_argument('-headless')

firefox_driver_path = "/PATH/TO/geckodriver"
service = Service(executable_path=firefox_driver_path)

driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("https://nac.nitk.ac.in:8090/")
except:
    sys.exit(0)

username = driver.find_element(By.NAME, "username")
username.clear()

password = driver.find_element(By.NAME, "password")
password.clear()

username.send_keys("ENTERTHEUSERNAMEHERE")
password.send_keys("ENTERTHEPASSWORDHERE")

driver.find_element(By.ID, "loginbutton").click()

print("Logged In.")

driver.close()
