class Carro:
    def __init__(self, passMax: int = 2, gasMax: int = 100):
        self.passMax = passMax
        self.gasMax = gasMax
        self.Pass = 0
        self.gas = 0
        self.km = 0

    def __str__(self):
        return f"pass: {self.Pass}, gas: {self.gas}, km: {self.km}"

    def enter(self):
        if self.Pass < self.passMax:
            self.Pass += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.Pass > 0:
            self.Pass -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, valueFuel: int):
        self.gas += valueFuel
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def driveDistance(self, distance: int):
        if self.Pass == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if distance > self.gas:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0
        else:
            self.km += distance
            self.gas -= distance

def main():
    carro = Carro()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            valueFuel: int = int(args[1])
            carro.fuel(valueFuel)
        elif args[0] == "drive":
            distance: int = int(args[1])
            carro.driveDistance(distance)

main()
    