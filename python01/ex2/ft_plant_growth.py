class Plant:
    def __init__(self, name, height, p_age):
        self.name = name
        self.height = height
        self.p_age = p_age

    def grow(self):
        self.height += 1
    def age(self):
        self.p_age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.p_age} days old")


plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]

k = 0
for i in plants:
    k += 1
print("=== Day1 ===")
for i in range(0, k):   
    plants[i].get_info()


print("=== Day7 ===")
for i in range(1, 7):
    for j in range(0, k):
        plants[j].age()
        plants[j].grow()
for j in range(0, k):
    plants[j].get_info()
    print(f"Growth this week: +{i}cm")

