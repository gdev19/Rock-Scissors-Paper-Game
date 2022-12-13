from random import choice


def my_game():
    """
        This function receives an input and with the help of random choice selects the computer's move and gives the
         result of  who won:

    """
    my_choice = input("r: rock, s: scissors, p: paper: ")
    s = ["r", "s", "p"]
    if my_choice not in s:
        return "wrong input:" "please, enter 'r', 's', 'p' "
    random_choice = choice(s)
    print("-> ", random_choice)
    if my_choice == random_choice:
        return "no one won"
    elif winner(my_choice, random_choice):
        return "you won"
    else:
        return "he won"


def winner(player, player2):
    """
        This feature contains all three winning outcomes for the player
        r>s
        p>r
        s>p
    """
    if (player == "r" and player2 == "s") or (player == "p" and player2 == "r") or (
            player == "s" and player2 == "p"):
        return True


score = {
    "me": 0,
    "he": 0
}

while True:
    result = my_game()
    print(result)
    if result == "you won":
        score["me"] += 1
        if score["me"] == 5:
            print(" you won 5 times ")
            break
    elif result == "he won":
        score["he"] += 1
        if score["he"] == 5:
            print("he won 5 times ")
            break

