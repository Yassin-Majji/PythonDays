class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    plants = [Plant("Rose", 25, 30)]
    initial_heights = []
    for plant in plants:
        initial_heights += [plant.height]

    print("=== Day 1 ===")
    for i in plants:
        print(i.get_info())

    for i in range(1, 7):
        for j in plants:
            Plant.age(j)
            j.grow()

    print("=== Day 7 ===")
    index = 0
    for plant in plants:
        print(plant.get_info())
        print(f"Growth this week: +{plant.height - initial_heights[index]}cm")
        index += 1
