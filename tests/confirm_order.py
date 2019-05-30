from selenium import webdriver
import unittest
import time
from pages.main_page import MainPage
from pages.choose_pizza_page import ChoosePizzaPage
from pages.pizza_options_page import PizzaOptionsPage
from pages.checkout_page import CheckoutPage
from sql.connect_to_db import check_sql


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
        pizza_options_page.click_checkout()
        checkout_page = CheckoutPage()
        checkout_page.check_checkout_text()
        checkout_page.input_first_name()
        checkout_page.input_last_name()
        checkout_page.input_address()
        checkout_page.input_card_number()
        checkout_page.input_csv()
        checkout_page.submit_order()
        check_sql(order_id, status)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
