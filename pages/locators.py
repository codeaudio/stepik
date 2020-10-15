from selenium.webdriver.common.by import By

class MainPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    text_of_bookname = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/strong')