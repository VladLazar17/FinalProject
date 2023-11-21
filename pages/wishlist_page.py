from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WishlistPage(BasePage):
    WISHLIST_TEXT = (By.CLASS_NAME, 'page-title')
    WISHLIST_EMPTY_TEXT = (By.CLASS_NAME, 'no-data')

    WISHLIST_PAGE_URL = 'https://demo.nopcommerce.com/wishlist'

    def navigate_to_wishlist_page(self):
        self.driver.get(self.WISHLIST_PAGE_URL)

    def is_wishlist_text_displayed(self):
        return self.is_element_displayed(self.WISHLIST_TEXT)

    def get_wishlist_empty_text(self):
        return self.get_element_text(self.WISHLIST_EMPTY_TEXT)
