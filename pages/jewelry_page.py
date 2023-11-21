from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class JewelryPage(BasePage):

    FLOWER_GIRL_BRACELET_WISHLIST_BUTTON = (
        By.XPATH, '//a[text()="Flower Girl Bracelet"]/following::button[text()="Add to wishlist"][1]')
    WISHLIST_MESSAGE = (By.CLASS_NAME, 'content')

    JEWELRY_PAGE_URL = 'https://demo.nopcommerce.com/jewelry'

    def navigate_to_jewelry_page(self):
        self.driver.get(self.JEWELRY_PAGE_URL)

    def add_the_flower_girl_bracelet_to_wishlist(self):
        self.click(self.FLOWER_GIRL_BRACELET_WISHLIST_BUTTON)

    def is_successful_added_to_wishlist(self):
        return self.is_element_displayed(self.WISHLIST_MESSAGE)

    def get_successful_added_to_wishlist_message(self):
        return self.get_element_text(self.WISHLIST_MESSAGE)
