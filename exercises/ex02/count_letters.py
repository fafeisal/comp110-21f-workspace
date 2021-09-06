"""Counting letters in a string."""

__author__ = "730474766"


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0
answer: int = 0

while i < len(word):
    if word[i] == letter:
        answer = answer + 1
        i = i + 1
    else:
        i = i + 1

print("Count: " + str(answer))