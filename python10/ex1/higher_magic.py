from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        print(f"Original: {power}, Amplified: {power * multiplier}")
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        return [spell(target, power) for spell in spells]
    return sequence


def strong_enough(target: str, power: int) -> bool:
    return power >= 50 and isinstance(target, str)


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    mega_fireball("Dragon", 10)

    print("\nTesting conditional caster...")
    conditional_spell = conditional_caster(strong_enough, fireball)
    print(conditional_spell("Dragon", 30))
    print(conditional_spell("Dragon", 60))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 20))


if __name__ == "__main__":
    main()
