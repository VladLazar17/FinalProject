from behave import *


@given('I am on the Wishlist page')
def step_impl(context):
    context.wishlist_page.navigate_to_wishlist_page()


@given('I am on the Jewelry Page')
def step_impl(context):
    context.jewelry_page.navigate_to_jewelry_page()


@when('I add to Wishlist the "Flower Girl Bracelet"')
def step_impl(context):
    context.jewelry_page.add_the_flower_girl_bracelet_to_wishlist()


@then('The Wishlist text displayed')
def step_impl(context):
    assert context.wishlist_page.is_wishlist_text_displayed()


@then('The Wishlist page contains the text "{empty_text}"')
def step_impl(context, empty_text):
    assert empty_text in context.wishlist_page.get_wishlist_empty_text()


@then('The successful adding to Wishlist message is displayed')
def step_impl(context):
    assert context.jewelry_page.is_successful_added_to_wishlist()


@then('The successful message contains "{added_product_text}"')
def step_impl(context, added_product_text):
    assert added_product_text in context.jewelry_page.get_successful_added_to_wishlist_message()


