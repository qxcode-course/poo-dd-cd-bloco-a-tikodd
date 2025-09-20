class  Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def getMaxWetness(self):
        if self.size == 'P':
            return 10
        if self.size == 'M':
            return 20
        if self.size == 'G':
            return 30
        return 0
        
    def dry(self, amount: int):
       self.wetness += amount
       if self.wetness > self.getMaxWetness():
           print ('toalha encharcada')
           self.wetness = self.getMaxWetness()
    
        
        

    def wringOut(self):
        self.wetness = 0

    def isdry(self):
        if self.wetness == 0:
            print ('true')
        else:
            print ('false')

    def show(self):
        print(self)

    def __str__(self):
        return f"{self.color} {self.size} {self.wetness}"

towel = Towel("Azul", "P")
towel.show()  # Azul P 0
towel.dry(5)
towel.show()  # Azul P 5
print(towel.isDry()) # False
towel.dry(5)
towel.show()  # Azul P 10
towel.dry(5) # msg: toalha encharcada
towel.show()  # Azul P 10

towel.wringOut()
towel.show()  # Azul P 0

towel = Towel("Verde", "G")
print(towel.isDry()) # True
towel.dry(30)
towel.show()  # Verde G 30
print(towel.isDry()) # False
towel.dry(1)  # msg: toalha encharcada

