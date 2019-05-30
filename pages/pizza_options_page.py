from locators.locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class PizzaOptionsPage():

    def __init__(self, driver):
        self.driver = driver

        #this part of code could be moved to locators file
        self.pizza_diameter = driver.find_element(By.XPATH, Locator.pizza_diameter)
        self.additional_component_cheese = driver.find_element(By.ID, Locator.additional_component_cheese)
        self.additional_component_meat = driver.find_element(By.ID, Locator.additional_component_meat)
        self.additional_component_tomato = driver.find_element(By.ID, Locator.additional_component_tomato)
        self.additional_component_cucumber = driver.find_element(By.ID, Locator.additional_component_cucumber)
        self.additional_component_corn = driver.find_element(By.ID, Locator.additional_component_corn)
        self.additional_info = driver.find_element(By.ID, Locator.additional_info)
        self.add_to_cart = driver.find_element(By.XPATH, Locator.add_to_cart)
        self.checkout_button = driver.find_element(By.CSS_SELECTOR, Locator.checkout_button)


    def click_diameter_of_pizza(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(By.XPATH, Locator.pizza_diameter))
        self.driver.pizza_diameter.click()

    def choose_additional_components(self):
        self.driver.additional_component_cheese.click()
        self.driver.additional_component_meat.click()
        self.driver.additional_component_tomato.click()
        self.driver.additional_component_cucumber.click()
        self.driver.additional_component_corn.click()

    def input_additional_info_text(self):
        self.driver.additional_info.send_keys("Please add to pizza more cheese.")

    def click_add_to_cart(self):
        self.driver.add_to_cart.click()

    def click_checkout(self):
        self.driver.checkout_button.click()

    def check_pizza_order(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, Locator.check_add_to_cart)))
        except NoSuchElementException:
            return False