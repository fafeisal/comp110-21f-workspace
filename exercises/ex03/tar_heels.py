"""An exercise in remainders and boolean logic."""

__author__ = "730474766"


user_input: int = int(input("Enter an int: "))
answer: str = "CAROLINA"

if user_input % 2 == 0 or user_input % 7 == 0:
    answer = ""
    if user_input % 2 == 0:
        answer += "TAR"
    if user_input % 2 == 0 and user_input % 7 == 0:
        answer += " "
    if user_input % 7 == 0:
        answer += "HEELS"
# if input % 2 == 0:
    # if input % 7 == 0:
        # print("TAR HEELS")
    # else:
        # print("TAR")
# else:
    # if input % 7 == 0:
        # print("HEELS")
    # else:
        # print("CAROLINA")

print(answer)