from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest

class SignUp(unittest.TestCase):

  def setUp(self):
    self.driver=webdriver.Chrome()

  def test_sign_up(self):
    driver = self.driver
    try:
        driver.get("https://authorized-partner.netlify.app/login")

    except Exception as ex:
       print(ex)

    else:
         driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/form/div[3]/div/a").click()
         time.sleep(5)
         driver.find_element(By.XPATH, '//*[@id="remember"]').click()
         time.sleep(5)
         driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[3]/a/button').click()
         time.sleep(5)


  def tearDown(self):
       self.driver.quit()

if __name__=="__main__":
    unittest.main()
           
