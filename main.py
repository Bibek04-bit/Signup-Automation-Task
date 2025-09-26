from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class SignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sign_up(self):
        driver = self.driver
        driver.maximize_window()
        try:
            driver.get("https://authorized-partner.netlify.app/login")
        except Exception as ex:
            print(ex)
        else:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/form/div[3]/div/a"))
            ).click()
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="remember"]'))
            ).click()
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[4]/div[3]/a/button'))
            ).click()
            time.sleep(2)
           #Frist Name
            fname = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'firstName'))
            )
            fname.clear()
            fname.send_keys('Bibek')
            time.sleep(2)
            # Last Name
            lname = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'lastName'))
            )
            lname.clear()
            lname.send_keys('Acharya')
            time.sleep(2)
             #Email
            Email = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'email'))
            )
            Email.clear()
            Email.send_keys(f"bibek{int(time.time())}@example.com")
            time.sleep(2)
            #Phone number
            Phone = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'phoneNumber'))
            )
            Phone.clear()
            Phone.send_keys(f"98{int(time.time()) % 10000000}")
            time.sleep(2)
           #PassWOrd
            PassW = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            PassW.clear()
            PassW.send_keys('Testmail100%')
            time.sleep(3)
           #Confirm Password
            CPassW = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'confirmPassword'))
            )
            CPassW.clear()
            CPassW.send_keys('Testmail100%')
            time.sleep(2)

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/div/div/div/div[2]/form/div[4]/button"))
            ).click()
            time.sleep(2)

            #Agency name
            AgencyName = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'agency_name'))
            )
            AgencyName.clear()
            AgencyName.send_keys('HackYourDreams')
            time.sleep(2)

            #Role in agency
            AgencyRole = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'role_in_agency'))
            )
            AgencyRole.send_keys('Intern')
            time.sleep(2)





           



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()