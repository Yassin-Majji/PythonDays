from ex0.Creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(HealCapability, Creature):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"


class Bloomelle(HealCapability, Creature):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"


class Shiftling(TransformCapability, Creature):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return "Shiftling returns to normal."
        else:
            return "Shiftling deos shift yet, it is Nomal"

    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."


class Morphagon(TransformCapability, Creature):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return "Morphagon stabilizes its form."
        else:
            return "Morphagon deos shift yet, it is Nomal"

    def attack(self) -> str:
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."
