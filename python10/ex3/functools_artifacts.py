from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError("Unknown operation")

    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatcher(arg):
        return "Unknown spell type"

    @dispatcher.register
    def _(arg: int):
        return f"Damage spell: {arg} damage"

    @dispatcher.register
    def _(arg: str):
        return f"Enchantment: {arg}"

    @dispatcher.register
    def _(arg: list):
        return f"Multi-cast: {len(arg)} spells"

    return dispatcher


def main():
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[Error] {e}")
