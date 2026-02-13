class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


list = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]
print("=== Garden Plant Registry ===")
for i in list:
    i.display()
