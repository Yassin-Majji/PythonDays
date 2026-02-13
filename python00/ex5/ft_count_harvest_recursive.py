def print_harvest_days(i: int, days: int) -> None:

    if i <= days:
        print("Day", i)
        print_harvest_days(i + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    print_harvest_days(1, days)
    print("Harvest time!")
