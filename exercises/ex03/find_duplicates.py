"""Finding duplicate letters in a word."""

__author__ = "730474766"


word: str = input("Enter a word: ")
i: int = 0
position: int = 0
answer: str = "Found duplicate: "
repeat_storage: int = 0


while i < len(word):
    letter: str = word[i]
    while position < len(word):
        if word[position] == letter and position != i:
            repeat_storage += 1
        position += 1
    position = 0
    i += 1

if repeat_storage > 0: 
    answer += "True"
else: 
    answer += "False"

print(answer)
