"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730474766"


class Simpy:
    """Object used for exercise."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize attributes for Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Produce a string representation for Simpy attributes."""
        return f"Simpy({self.values})"

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Create a new jupyter using Simpy object additon."""
        combined: list[float] = []
        # Turn int into float for prewritten jupyter notebook tests
        if isinstance(rhs, int):
            rhs = float(rhs)
        if isinstance(rhs, float):
            for value in self.values:
                combined.append(value + rhs)
        else:
            if len(self.values) != len(rhs.values):
                assert IndexError
            for index, value in enumerate(self.values):
                combined.append(value + rhs.values[index])
        new: Simpy = Simpy(combined)
        return new

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Create a new jupyter using Simpy object additon."""
        combined: list[float] = []
        # Turn int into float for prewritten jupyter notebook tests
        if isinstance(rhs, int):
            rhs = float(rhs)
        if isinstance(rhs, float):
            for value in self.values:
                combined.append(value ** rhs)
        else:
            if len(self.values) != len(rhs.values):
                assert IndexError
            for index, value in enumerate(self.values):
                combined.append(value ** rhs.values[index])
        new: Simpy = Simpy(combined)
        return new

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Create a new jupyter using Simpy object additon."""
        true_false: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                true_false.append(value == rhs)
        else:
            if len(self.values) != len(rhs.values):
                assert IndexError
            for index, value in enumerate(self.values):
                true_false.append(value == rhs.values[index])
        return true_false

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Create a new jupyter using Simpy object additon."""
        true_false: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                true_false.append(value > rhs)
        else:
            if len(self.values) != len(rhs.values):
                assert IndexError
            for index, value in enumerate(self.values):
                true_false.append(value > rhs.values[index])
        return true_false

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use subscription notation with object Simpy."""
        mask: list[float] = []
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            for index, value in enumerate(self.values):
                if rhs[index]:
                    mask.append(value)
            new: Simpy = Simpy(mask)
            return new

    def fill(self, value: float, times: int) -> None:
        """Changes values of object to repeat value given a given number of times."""
        j: int = 0
        while j < len(self.values):
            self.values.pop(len(self.values) - 1)
        i: int = 0
        while i < times:
            self.values.append(value)
            i += 1
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Set values as an incremental list based on input metrics."""
        if step == 0.0:
            assert step != 0.0
        j: int = 0
        while j < len(self.values):
            self.values.pop(len(self.values) - 1)
        i: int = 0
        while i < ((stop - start) / step):
            if start in self.values:
                self.values.append(self.values[(len(self.values) - 1)] + step)
            else: 
                self.values.append(start)
            i += 1
        return None

    def sum(self) -> float:
        """Add up Simpy values with built-in Python function."""
        return sum(self.values)