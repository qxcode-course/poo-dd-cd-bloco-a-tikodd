class carro:
    def __init__(self):
        self.Pass: int = 0
        self.gas: int = 0
        self.km: int = 0

    def __str__(self):
        return f"Pass:{self.Pass}, gas:{self.gas}, km:{self.km}"
    
    def show(self):
        print(str(self))

def main():
    car = carro()
    while True:
        line = input()
        if line == "end":
            break

        print("$" + line)
        if line == "show":
            car.show()

main()

    