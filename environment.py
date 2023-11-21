from browser import Browser
from pages.home_page import HomePage
from pages.jewelry_page import JewelryPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage
from pages.wishlist_page import WishlistPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.search_results_page = SearchResultsPage()
    context.home_page = HomePage()
    context.register_page = RegisterPage()
    context.wishlist_page = WishlistPage()
    context.jewelry_page = JewelryPage()


def after_all(context):
    context.browser.close()
