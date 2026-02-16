class Plant:
    def __init__(self, name: str, height: int, p_age: int) -> None:
        self.name = name
        self.height = height
        self.p_age = p_age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.p_age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.p_age} days old")


if __name__ == "__main__":
    plants = [Plant("Rose", 25, 30),]
    days = 7
    print("=== Day1 ===")
    for i in plants:
        i.get_info()
    print("=== Day7 ===")
    for i in range(1, 7):
        for j in plants:
            j.age()
            j.grow()
    for j in plants:
        j.get_info()
        print(f"Growth this week: +{days - 1}cm")
