from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
import requests
import re

def get_temp_email():
    # Get a random address from mail.tm
    domain_resp = requests.get("https://api.mail.tm/domains")
    domain = domain_resp.json()["hydra:member"][0]["domain"]
    username = f"bibek{int(time.time())}"
    address = f"{username}@{domain}"
    password = "Testmail100%"
    # Register the address
    requests.post("https://api.mail.tm/accounts", json={
        "address": address,
        "password": password
    })
    # Get token
    token_resp = requests.post("https://api.mail.tm/token", json={
        "address": address,
        "password": password
    })
    token = token_resp.json()["token"]
    return address, token

def get_otp_from_email(token):
    headers = {"Authorization": f"Bearer {token}"}
    for _ in range(30):  # Try for 30 seconds
        msgs = requests.get("https://api.mail.tm/messages", headers=headers).json()
        if msgs["hydra:totalItems"] > 0:
            msg_id = msgs["hydra:member"][0]["id"]
            msg = requests.get(f"https://api.mail.tm/messages/{msg_id}", headers=headers).json()
            otp_match = re.search(r"\b\d{4,6}\b", msg["text"])
            if otp_match:
                return otp_match.group(0)
        time.sleep(1)
    return None

class SignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sign_up(self):
        driver = self.driver
        driver.maximize_window()
        email, token = get_temp_email()
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
            fname = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'firstName'))
            )
            fname.clear()
            fname.send_keys('Bibek')
            time.sleep(2)
            lname = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'lastName'))
            )
            lname.clear()
            lname.send_keys('Acharya')
            time.sleep(2)
            Email = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'email'))
            )
            Email.clear()
            Email.send_keys(email)
            time.sleep(2)
            Phone = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'phoneNumber'))
            )
            Phone.clear()
            Phone.send_keys(f"98{int(time.time()) % 10000000}")
            time.sleep(2)
            PassW = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            PassW.clear()
            PassW.send_keys('Testmail100%')
            time.sleep(3)
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

             # Wait for OTP field and auto-fill OTP
            otp_field = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div/div[2]/div/form/div[1]/div[2]/input'))  # Update selector if needed
            )
            otp = get_otp_from_email(token)
            if otp:
                otp_field.send_keys(otp)
                time.sleep(2)
            else:
                print("OTP not received!")

            Verify= WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[4]/div/div/div/div[2]/div/form/div[2]/button'))
            ).click()
            time.sleep(2)


            AgencyName = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'agency_name'))
            )
            AgencyName.clear()
            AgencyName.send_keys('HackYourDreams')
            time.sleep(2)


            AgencyRole = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'role_in_agency'))
            )
            AgencyRole.send_keys('Intern')
            time.sleep(2)


            AgencyEmail = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'agency_email'))
            )
            AgencyEmail.clear()
            AgencyEmail.send_keys(f"test{int(time.time())}@example.com")
            time.sleep(2)

            AgencyWeb = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'agency_website'))
            )
            AgencyWeb.clear()
            AgencyWeb.send_keys(f'testsite{int(time.time())}.com')
            time.sleep(2)

            AgencyAddr = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'agency_address'))
            )
            AgencyAddr.clear()
            AgencyAddr.send_keys('Kathmandu')
            time.sleep(2)

            Region = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[4]/div/div/div/div[2]/form/div[3]/div[2]/button'))
            )
            Region.click()
            time.sleep(2)

            # Wait for any input with placeholder containing 'Search'
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Search")]'))
            )
            search_input.clear()
            search_input.send_keys('Nepal')
            time.sleep(2)

            # Wait for the country option containing 'Nepal' and click it
            country_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Nepal")]'))
            )
            country_option.click()
            time.sleep(2)

            random = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[4]/div/div/div/div[2]/form/div[3]/div[2]/button'))
            )
            random.click()
            time.sleep(2)


            Nxt = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[4]/div/div/div/div[2]/form/div[4]/button[2]'))
            )
            Nxt.click()
            time.sleep(2)

            # Wait for the Experience button by visible text
            Exp = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Experience")]'))
            )
            Exp.click()
            time.sleep(2)

            # Wait for the selection field by placeholder or label
            Sel = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//input[contains(@placeholder, "Select")]'))
            )
            Sel.click()
            time.sleep(2)






           

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()