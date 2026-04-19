import alchemy.elements as m


def healing_potion() -> str:
    return (f"Healing potion brewed with {m.create_fire()}"
            f" and {m.create_water()}"
            )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with {m.create_earth()}"
        f" and {m.create_fire()}"
            )


def invisibility_potion() -> str:
    return (
        f"Invisibility potion brewed with {m.create_air()}"
        f" and {m.create_water()}")


def wisdom_potion() -> str:
    return (
        f"Wisdom potion brewed with all elements: {m.create_fire()} "
        f"{m.create_water} {m.create_earth} {m.create_air()}"
        )
