class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __strs__(self):
        return f"{self.species}:{self.age}:{self.sound}"
    
def main():
    