class Animal:
    def __init__(self, species: str, sound: str): #construtor
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __strs__(self):
        return f"{self.species}:{self.age}:{self.sound}"
    
    def ageBy (self, increment: int):
        self.age += increment
        if self.age >= 4:
            print (f"warning:{self.species} morreu")
            self.age = self.age

def main():
    bicho = Animal("","")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split (" ")
        if args [0] == "end":
            break
        elif args [0] == "init":
            species = args[1]
            sound = args[2]
            bicho = Animal(species,sound)
        elif args [0] == "show":
            print(bicho)
        elif args [0] == "grow":
            increment: int = int(args[1])
            bicho.ageBy(increment)
main()
