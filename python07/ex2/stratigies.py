from .strategy import BattleStrategy
from ex0.Creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import cast


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise Exception(
                f"Invalid Creature '{creature.name}' "
                "for normal strategy"
                )


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            t_creature = cast(TransformCapability, creature)
            print(t_creature.transform())
            print(creature.attack())
            print(t_creature.revert())
        else:
            raise Exception(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
                )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            t_creature = cast(HealCapability, creature)
            print(creature.attack())
            print(t_creature.heal())
        else:
            raise Exception(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy"
                )
