
Feature: NatGeo (Natural Language, test)

@test1
Scenario: Navigate to natgeo
        Given I am at the natgeo homepage
        Then the logo should be displayed

@test2
Scenario: Search in natgeo
        Given I am at the natgeo homepage
        When I fill de search and submit it
        Then I should see the results

@test3
Scenario: Search in natgeo
        Given I am at the natgeo homepage
        When I click in the animals tab
        And I click in domestic dogs
        Then I wait