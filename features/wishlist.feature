Feature: Test the functionality of the Wishlist page

  @wishlist
  Scenario: Check that the wishlist is empty
    Given I am on the Wishlist page
    Then The Wishlist text displayed
    Then The Wishlist page contains the text "The wishlist is empty!"

  @wishlist
  Scenario: Check that the "The product has been added to your wishlist" message is displayed when adding a product to Wishlist
    Given I am on the Jewelry Page
    When I add to Wishlist the "Flower Girl Bracelet"
    Then The successful adding to Wishlist message is displayed
    Then The successful message contains "The product has been added to your wishlist"