# Autologin Captive Portal

## Raspberry Pi 

### 1. Install Dependencies
```
sudo apt-get upgrade
sudo apt-get update
sudo apt-get install iceweasel
sudo pip3 install selenium
sudo python -m pip install selenium
sudo apt install firefox-esr
```
### 2. Install Geckodriver

#### Check the geckodriver version required for your firefox version:
https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html

Here version of firefox in Pi was `firefox v78.0`, Hence `geckodriver v0.21.0` was installed 

1. Download the geckodriver from mozilla: 
https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-arm7hf.tar.gz


2. Extract the downloaded file
```
tar -xzvf geckodriver-v0.21.0-arm7hf.tar.gz
cd geckodriver-v0.21.0-arm7hf.tar.gz
```

3. Copy file to /usr/local/bin
```
sudo cp geckodriver /usr/local/bin/
```
4. Test the geckodriver installation
```
python3
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
```
A Browser pops up (and stays without any errors)

### 3. Run Python File for Auto Login

1. Clone the Repo
```
git clone https://github.com/esmanish/nac_login.git
```
Move both python and shell script to home folder

2. Put appropriate captive-portal link and login credentials in `nac_login.py`, then
```
sudo chmod +x nac_login.py
python nac_login.py
```
OR
```
sudo chmod +x nac_login.sh
sh nac_login.sh
```
Logged In will display in terminal

### 4. Headless/RunOnStartup Setup

Crontab is used to run the shell script on boot 

1. Open the crontab
```
sudo crontab -e
```

2. Paste the following at bottom
```
@reboot sleep 10; cd /home/pi && bash nac_login.sh &
```

3. Reboot
After reboot pi will automatically connect to the nac


## PC/Laptops 
 ...
