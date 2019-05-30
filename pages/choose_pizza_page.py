from locators.locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class ChoosePizzaPage():

    def __init__(self, driver):
        self.driver = driver

        #this part of code could be moved to locators file
        self.name_of_pizza = driver.find_element(By.LINK_TEXT, Locator.name_of_pizza)

    def click_name_of_pizza(self):
        self.name_of_pizza.click()

    #asserts could be put into main file
    def check_order_pizza_page(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Locator.order_pizza_text)))
        except NoSuchElementException:
            return False

    def check_new_pizza_opened(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Locator.new_pizza_text)))
        except NoSuchElementException:
            return False
