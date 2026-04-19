class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    total_plants = 0
    plants = []
    for name, height, age in plants_data:
        plants += [Plant(name, height, age)]
        total_plants += 1

    print("=== Plant Factory Output ===")
    for i in plants:
        i.display()
    print(f"\nTotal plants created: {total_plants}")
