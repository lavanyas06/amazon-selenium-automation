from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
  
        self.signin_button = (By.XPATH, '//*[@id="nav-link-accountList"]')
        self.email_box = (By.XPATH, '//*[@id="ap_email_login"]')
        self.continue_btn = (By.XPATH, '//*[@id="continue"]/span/input')
        self.password_box = (By.XPATH, '//*[@id="ap_password"]')
        self.signin_btn = (By.XPATH, '//*[@id="signInSubmit"]')

    def open_login_page(self):
        self.driver.get("https://www.amazon.in")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.signin_button)
        )
        self.driver.find_element(*self.signin_button).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_box).send_keys(email)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.continue_btn)
        )

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.password_box)
        )

    def enter_password(self, password):
        self.driver.find_element(*self.password_box).send_keys(password)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.signin_btn)
        )

    def click_signin(self):
        self.driver.find_element(*self.signin_btn).click()
        WebDriverWait(self.driver, 20).until(
            EC.url_changes("https://www.amazon.in/ap/signin")  
        )
