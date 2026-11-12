from items import Weapon


class Character:
    def __init__(self, name: str, hp: int = 100, base_damage: int = 10,
                 weapon: Weapon | None = None) -> None:
        self.name = name
        self._hp = hp
        self.base_damage = base_damage
        self.weapon = weapon  # valgfritt våpen (oppgave 3)

    @property
    def is_alive(self) -> bool:
        return self._hp > 0

    def take_damage(self, damage: int) -> None:
        self._hp = max(0, self._hp - damage)

    def heal(self, amount: int) -> None:
        self._hp += amount

    def attack(self, target: "Character") -> None:
        # Bruker våpenets skade hvis utstyrt, ellers standard skade
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.base_damage
        target.take_damage(damage)


if __name__ == "__main__":
    from dice import Dice

    sword = Weapon("Sword", Dice(8))
    hero = Character("Hero", weapon=sword)
    enemy = Character("Goblin")

    hero.attack(enemy)
    print(enemy._hp)  # 92 til 99
