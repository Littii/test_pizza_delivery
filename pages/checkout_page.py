from locators.locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

        #this part of code could be moved to locators file
        self.first_name = driver.find_element(By.ID, Locator.first_name)
        self.last_name = driver.find_element(By.ID, Locator.last_name)
        self.address = driver.find_element(By.ID, Locator.address)
        self.card_number = driver.find_element(By.ID, Locator.card_number)
        self.card_csv = driver.find_element(By.ID, Locator.card_csv)
        self.submit_order = driver.find_element(By.CSS_SELECTOR, Locator.submit_order)

    def input_first_name(self):
        self.driver.first_name.send_keys("John")

    def input_last_name(self):
        self.driver.last_name.send_keys("Dou")

    def input_address(self):
        self.driver.address.send_keys("Green street, home 25")

    def input_card_number(self):
        self.driver.card_number.send_keys("4111111111111111")

    def input_csv(self):
        self.driver.card_csv.send_keys("111")

    def submit_order(self):
        self.driver.submit_order.click()

    def check_checkout_text(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Locator.checkout_text)))
        except NoSuchElementException:
            return False