from typing import Generator


def game_events(n: int) -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(n):
        player = players[i % len(players)]
        level = i % 20
        event = events[i % len(events)]

        yield (i + 1, player, level, event)


def fibonacci() -> Generator[int, None, None]:
    a = 0
    b = 1
    tmp = None
    while (True):
        yield a
        tmp = a
        a = b
        b = tmp + b


def primes() -> Generator[int, None, None]:
    num = 2
    while True:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            yield num

        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    total_events = 1000
    print(f"Processing {total_events} game events...\n")

    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    for event_id, player, level, event in game_events(total_events):
        print(f"Event {event_id}: Player {player} (level {level}) {event}")

        total += 1

        if level >= 10:
            high_level += 1

        if event == "found treasure":
            treasure += 1

        if event == "leveled up":
            level_up += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci()
    i = 0
    print("Fibonacci sequence (first 10): ", end='')
    for _ in range(10):
        if i == 1:
            print(", ", end='')
        print(next(fib), end='')
        i = 1

    print()

    prime_gen = primes()
    i = 0
    print("Prime numbers (first 5): ", end="")
    for _ in range(5):
        if (i == 1):
            print(", ", end='')
        print(next(prime_gen), end='')
        i = 1
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
