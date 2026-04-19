from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2.stratigies import TransformCapability, HealCapability
from ex0.factory import CreatureFactory
from ex0.Creature import Creature
from typing import cast


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base: Creature = factory.create_base()
    evolved: Creature = factory.create_evolved()

    c_base = cast(HealCapability, base)
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(c_base.heal())

    c_evolved = cast(HealCapability, evolved)
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(c_evolved.heal())
    print()


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base: Creature = factory.create_base()
    evolved: Creature = factory.create_evolved()

    c_base = cast(TransformCapability, base)
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(c_base.transform())
    print(base.attack())
    print(c_base.revert())

    c_evolved = cast(TransformCapability, evolved)
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(c_evolved.transform())
    print(evolved.attack())
    print(c_evolved.revert())


def main() -> None:
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    test_healing(heal)
    test_transform(transform)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error", e)
