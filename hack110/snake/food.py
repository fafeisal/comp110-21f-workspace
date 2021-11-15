import pygame as py
import math
from vector import Vector
class Food:
    """Objects player is defending against."""
    position: Vector
    color: tuple

    def __init__(self, position: Vector, color: tuple):
        self.position = position
        self.color = color