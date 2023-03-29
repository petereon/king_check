Feature: King gets check

    Scenario: Pawn checks King
        Given King is on A1 
        And Pawn is on B3
        When Pawn moves on B2
        Then King is in check
