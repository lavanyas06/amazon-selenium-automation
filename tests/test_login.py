from utils.driver_setup import get_driver
from pages.login_page import LoginPage
import time

def test_login():
    driver = get_driver()
    login_page = LoginPage(driver)

    login_page.open_login_page()

    # STEP 1: Enter email
    login_page.enter_email("")  # <-- Replace with your email
    login_page.click_continue()

    # STEP 2: Enter password
    login_page.enter_password("")  # <-- Replace with your password
    login_page.click_signin()

    time.sleep(5)  # wait to see result manually
    driver.quit()
