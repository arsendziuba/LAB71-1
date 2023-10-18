class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number

    def storage_place(self):
        if self.number < 0:
            return "out of stock"
        elif 0 <= self.number < 100:
            return "warehouse"
        else:
            return "Remote warehouse"

# Creating two Building objects
building1 = Building("Bricks", "Red", 150)
building2 = Building("Wood", "Brown", 50)

# Testing the storage_place method
print(f"{building1.material} is in {building1.storage_place()}")
print(f"{building2.material} is in {building2.storage_place()}")
