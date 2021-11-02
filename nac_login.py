import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",options=options)
try: 
	driver.get("Replace_with_captive_link")
except:
	sys.exit(0)

username = driver.find_element_by_name("username")
username.clear()

password = driver.find_element_by_name("password")
password.clear()

username.send_keys("Replace with credential-username")
password.send_keys("Replace with credential-password")

driver.find_element_by_id("loginbutton").click()

print ("Logged In.")

driver.close()