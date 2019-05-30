from selenium import webdriver
import unittest
import time
from pages.main_page import MainPage


class openPagePizzaDelivery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_choose_pizza_type(self):
        driver = self.driver
        driver.get("http://www.orderpizza.com")
        assert "Order pizza in our shop." in driver.title
        main_page = MainPage(driver)
        main_page.check_main_page_text()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
