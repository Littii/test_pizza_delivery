from locators.locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class MainPage():

    def __init__(self, driver):
        self.driver = driver

        #this part of code could be moved to locators file
        self.order_pizza_now = driver.find_element(By.LINK_TEXT, Locator.order_pizza_now)

    def click_order_pizza_now(self):
        self.driver.order_pizza_now.click()

    # assert could be put into main file
    def check_main_page_text(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Locator.main_page_text)))
        except NoSuchElementException:
            return False