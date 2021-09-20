"""Choose your own adventure game from first project."""

__author__ = "730474766"


from random import randint
player: str = ""


def greet() -> None:
    """Function for greeting player before game."""
    global player
    player = input("What is your name? ")
    print(f"Welcome {player}!")
    print(f"This is a game meant to teach excellent morals one gold star at a time. \nThroughout one cookie filled tale, you will be given gold stars \nfor every RIGHT decision. Good luck, {player}! :)")
    return None


def steal(points: int) -> int:
    """Second event in the case of stealing cookies."""
    print(f"Great job, {player}! Now you can make sure that no cookies go to waste! \nThere's no way your brother's friends could have finished all of them.")
    print("But why steal JUST one?")
    cookie_points: int = points * int(input(f"{player}, how many do you wish to steal: "))
    if cookie_points > 0:
        print("Great job! You get so many gold stars!")
    else:
        DISAPPOINTMENT: str = "\U0001F61E"
        print(f"{DISAPPOINTMENT} You must not love your family very much, {player}. \nNo more gold stars for {player}!")
        cookie_points = 0
    return cookie_points


def destroy() -> int:
    """Second event in the case of destroying cookies."""
    print(f"Great job, {player}! Now you can make sure your brother doesn't get a reward for no reason! \nAfter all, he's not the one who's collecting gold stars.")
    # cookie_points: int = randint(10, 100)
    # return cookie_points
    global points
    points += randint(10, 100)
    project: str = input(f"Would you also like to later destroy your brother's project? \nType \'YES\' if you would {player}: ")
    if project == "YES":
        points += 200
        print(f"Excellent choice, {player}!")
    else: 
        points += -10
        print(f"Pity...I expected more from you, {player}.")
    return points


def trash(points: int) -> int:
    """Second event in the case of throwing away cookies."""
    print(f"Great job, {player}! Now make sure to tell your mom that your brother did it. \nWe have to make sure that she remembers how naughty he is!")
    cookie_points: int = points * randint(300, 500)
    cupcakes: str = input(f"Oh, {player}! There's a tray of cupcakes too! Want to throw those away? \nType \'YES\': ")
    if cupcakes == "YES":
        cookie_points += 1000
        print("Awesome choice!")
    else:
        cookie_points += -100
        print("Aw, that was a sad choice.")
    return cookie_points


def game() -> None:
    """Main function to define morals with cookies game."""
    global points
    # points: int = 0
    points = 0
    cont: str = ""
    greet()
    print(f"You, {player}, are sitting by the counter. \nwhere your mother just recently placed a tray of cookies \nfor your brother's playdate.")
    print(f"{player}, would you like to: ")
    print("1. Steal a cookie")
    print("2. Knock the cookies off the counter")
    print("3. Throw the cookies away")
    print("4. Quit the game")
    cookies_answer: str = input(f"{player}, type the number of your choice: ")
    while cookies_answer != "1" and cookies_answer != "2" and cookies_answer != "3" and cookies_answer != "4":
        cookies_answer = (input(f"Oops, {player}, that wasn't an option. \nTry again: "))
    if cookies_answer == "1" or cookies_answer == "2" or cookies_answer == "3":
        points += 1
        if cookies_answer == "1":
            points += steal(points)
        if cookies_answer == "2":
            # points += destroy()
            destroy()
        if cookies_answer == "3":
            points += trash(points)
        print(f"Gold Stars: {points}")
        cont = input("Would you like to try again? \nIf you do, type \'Yes\': ")
        if cont != "Yes":
            print(f"Bye bye, {player}, have a good day! \n(and maybe come play again sometime)")
        while cont == "Yes":
            game()
            cont = ""
    else:
        print(f"Oh! Okay {player}, I guess you leave with {points} gold stars!")
        cont = ""
    return None


if __name__ == "__main__":
    game()