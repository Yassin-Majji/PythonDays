from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    creature_types = [base, evolved]
    for t in creature_types:
        print(t.describe())
        print(t.attack())
    print()


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    test_factory(aqua)
    test_battle(flame, aqua)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
