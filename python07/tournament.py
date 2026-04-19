from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy
from ex0.factories import CreatureFactory


def tournament(opponents: list[
                tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print("\n* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                strategy1.act(c1)
                strategy2.act(c2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:

    print("Tournament 0 (basic)")
    opponents: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    tournament(opponents)

    print("\nTournament 1 (error)")
    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament(opponents)

    print("\nTournament 2 (multiple)")
    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    tournament(opponents)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error: ", e)
