import random


class Dice:
    """En n-sidig terning."""

    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """Kaster terningen og returnerer et tall mellom 1 og sides."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Gjør at d20() fungerer likt som d20.roll()."""
        return self.roll()
