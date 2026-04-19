class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def plant_data(self, type: str) -> None:
        print(
            f"{self.name} ({type}): {self.height}cm, "
            f"{self.age} days, ", end=""
            )


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def plant_data(self) -> None:
        super().plant_data("Flower")
        print(f"{self.color} color")

    def poly(self) -> None:
        self.bloom()

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def plant_data(self) -> None:
        super().plant_data("Tree")
        print(f"{self.trunk_diameter}cm diameter")

    def poly(self) -> None:
        self.produce_shade()

    def produce_shade(self) -> None:
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def plant_data(self) -> None:
        super().plant_data("Vegetable")
        print(f"{self.harvest_season} harvest")

    def poly(self) -> None:
        self.food_value()

    def food_value(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 15, 40, "yellow"),

        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 800, 3000, 30),

        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "winter", "vitamin A"),
    ]

    for i in plants:
        i.plant_data()
        i.poly()
        print()
