from selenium import webdriver
import unittest
import time
from pages.main_page import MainPage
from pages.choose_pizza_page import ChoosePizzaPage
from pages.pizza_options_page import PizzaOptionsPage


class openPagePizzaDelivery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testUserChoosesPizzaType(self):
        driver = self.driver
        driver.get("http://www.orderpizza.com")
        assert "Order pizza in our shop." in driver.title
        main_page = MainPage(driver)
        main_page.clickOrderPizzaNow()
        choose_pizza_page = ChoosePizzaPage(driver)
        choose_pizza_page.check_order_pizza_page()
        choose_pizza_page.click_name_of_pizza()
        choose_pizza_page.check_new_pizza_opened()
        pizza_options_page = PizzaOptionsPage()
        pizza_options_page.click_diameter_of_pizza()
        pizza_options_page.choose_additional_components()
        pizza_options_page.input_additional_info_text()
        pizza_options_page.click_add_to_cart()
        pizza_options_page.check_pizza_order()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
