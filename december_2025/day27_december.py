"""

Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

    The input strings will always be "Rock", "Paper", or "Scissors".
    "Rock" beats "Scissors".
    "Paper" beats "Rock".
    "Scissors" beats "Paper".

Return:

    "Player 1 wins" if Player 1 wins.
    "Player 2 wins" if Player 2 wins.
    "Tie" if both players choose the same option.

"""
def rock_paper_scissors(player1, player2):
    outcomes = {
        ("Rock", "Scissors"): "Player 1 wins",
        ("Scissors", "Paper"): "Player 1 wins",
        ("Paper", "Rock"): "Player 1 wins",
        ("Scissors", "Rock"): "Player 2 wins",
        ("Paper", "Scissors"): "Player 2 wins",
        ("Rock", "Paper"): "Player 2 wins",
    }

    if player1 == player2:
        return "Tie"
    return outcomes.get((player1, player2), "Invalid input")