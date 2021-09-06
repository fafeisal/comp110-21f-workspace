"""Repeating a beat in a loop."""

__author__ = "730474766"


beat: str = input("What beat do you want to repeat? ")
repeats: int = int(input("How many times do you want to repeat it? "))
i: int = 1
repeated_beat: str = ""

if repeats > 0:
    while i <= repeats:
        if i < repeats:
            repeated_beat = repeated_beat + beat + " "
        else:
            repeated_beat = repeated_beat + beat
        i = i + 1
    print(repeated_beat)

else:
    print("No beat...")