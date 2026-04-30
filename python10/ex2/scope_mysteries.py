from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def add_power(power_to_add: int) -> int:
        nonlocal power
        power += power_to_add
        return power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    for i in range(1, 3):
        print(f"counter_a call {i}: {counter_a()}")

    counter_b = mage_counter()
    for i in range(1, 2):
        print(f"counter_b call {i}: {counter_b()}")

    print()

    print("Testing spell accumulator...")
    initial_power = 100
    add_powers = [20, 30]
    add_to_power = spell_accumulator(initial_power)
    for i in range(2):
        print(
            f"Base {initial_power}, add {add_powers[i]}:"
            f" {add_to_power(add_powers[i])}"
            )

    print()

    print("Testing enchantment factory...")
    enchantments_type = ['Flaming', 'Frozen']
    items_name = ['Sword', 'Shield']
    for i in range(len(items_name)):
        ench = enchantment_factory(enchantments_type[i])
        print(ench(items_name[i]))

    print()

    print("Testing memory vault...")
    stor_call = memory_vault()
    data = {'secret': 42}
    for k, v in data.items():
        stor_call['store'](k, v)
        print(f"Store '{k}' = {v}")
    data['unknown'] = 'none'
    for k in data.keys():
        stor_call['recall'](k)
        print(f"Recall '{k}': {stor_call['recall'](k)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[Error] {e}")
