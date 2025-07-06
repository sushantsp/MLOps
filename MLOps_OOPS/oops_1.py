class employee:

    # dunder menthods - Constructor
    def __init__(self):
        print("Following attributes will be defined")
        self.name = "Naam"
        self.id = 25
        self.salary = "$50k"
        self.designation = "ML Engineer"

        print(f"{self.name, self.id, self.salary, self.designation}")

    def travel(self, destination):
        print(f"Employee is now travellling to {destination}")

sam = employee()

print(sam.name)

print(sam.travel("Netherlands"))