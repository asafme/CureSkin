# Created by jessicamenashe at 4/20/23
Feature: CureSkin Product Search


  Scenario: Search Results are Shown
    Given Open CureSkin main page
    When Close popup window
    When Click on search button
    And Input text CureSkin gel
    Then Verify Product results for Cureskin gel are shown