class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} sings")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} moos")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} roars")

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def perform_duties(self):
        pass

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}  {animal.species}")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}  {animal.species}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное {animal.name},  {animal.species}, в зоопарке.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен {employee.name}, служащий {employee.role}, в зоопарке.")

    def show_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.species})")

    def show_employees(self):
        print("Employees in the zoo:")
        for employee in self.employees:
            print(f"- {employee.name} ({employee.role})")


zoo = Zoo()


sparrow = Bird("Шустряк", "sparrow")
cow = Mammal("Бестия", "cow")
crocodile = Reptile("Пират", "crocodile")

zoo.add_animal(sparrow)
zoo.add_animal(cow)
zoo.add_animal(crocodile)


keeper = ZooKeeper("Петрович")
vet = Veterinarian("Dr. Пётр")

zoo.add_employee(keeper)
zoo.add_employee(vet)


zoo.show_animals()
zoo.show_employees()


keeper.feed_animal(sparrow)
vet.heal_animal(crocodile)