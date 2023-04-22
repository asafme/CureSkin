# Created by jessicamenashe at 4/21/23
Feature: CureSkin UI Features

  Scenario: Verify that UI features are shown on product page
    Given Open CureSkin main page
    When Close popup window
    And Click on search button
    When Input text under eye gel
    And Click on the product from search results
    Then Verify image is present
    And Verify price is present
    And Verify reviews are present
    And Verify add to cart is present
    And Verify buy it now button is present