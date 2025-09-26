from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#https://sites.google.com/chromium.org/driver/
service = Service(executable_path= "chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://authorized-partner.netlify.app/login")

time.sleep(15)

driver.quit()