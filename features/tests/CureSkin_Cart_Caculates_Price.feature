# Created by jessicamenashe at 4/24/23
Feature: Cart calculates price


  Scenario: Verify that cart calculates price for the same product.
    Given Open product details page of CureSkin Gentle Cleanse Face Foam
    When Click on Add to Cart button
    And Store the current price
    Then Click plus icon to increase product quantity
    And Verify price has doubled
    And Verify cart has 2 items
