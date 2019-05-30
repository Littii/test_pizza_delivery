class Locator(object):
    #main_page locators
    order_pizza_now = "Order pizza now"
    main_page_text = "//div[text()='Buy pizza online here!']"

    #choose pizza page locators
    #choose name of pizza: Spinach Combo, Vegetarian, Cheese Pizza
    name_of_pizza = "Hawaiian"
    new_pizza_text = "//table[@id='pizza_choosing']"
    order_pizza_text = "//span[text()='You can choose your pizza here']"

    #pizza options page locators
    pizza_diameter = "//select[@id='diameter']/option[@value='20']"
    additional_component_cheese = "cheese"
    additional_component_meat = "meat"
    additional_component_tomato = "tomato"
    additional_component_cucumber = "cucumber"
    additional_component_corn = "corn"
    additional_info = "additional_info"
    add_to_cart = "//*[text()='Add To Cart']"
    check_add_to_cart = "new_order_id"
    checkout_button = '.button .checkout'

    #checkout page locators
    first_name = "first_name"
    last_name = "last_name"
    adress = "adress"
    card_number = "card_id"
    card_csv = "csv_id"
    submit_order = "input[name='submit_order'][type='submit']"
    checkout_text_info - "//div[text()='Please input payment info']"