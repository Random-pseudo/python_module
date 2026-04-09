import random

def main():
    print("=== Game Data Alchemist ===")
    initial_players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print("Initial list of players: " + initial_players)
    all_capitalized = [player.capitalize() for player in initial_players]
    print("New list with all names capitalized: " + str(all_capitalized))
    print()
    only_capitalized = [player for player in all_capitalized if player[0].isupper()]
    print("New list of capitalized names only: " + only_capitalized)
    print()
    score_dict = {name : random.randint(0, 999) for name in all_capitalized}
    print( "Score dict: " + score_dict)
    print()
    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print("Score average is " + average)
    print()
    high_scores = {name : score for name, score in score_dict.items() if score > average}
    print("High scores: " + str(high_scores))
    