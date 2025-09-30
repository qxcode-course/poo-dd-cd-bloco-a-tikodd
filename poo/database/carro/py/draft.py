class car:
    def __init__(self, Pass: int, gas: int, km: int):
        self.Pass: int = 0
        self.gas: int = 0
        self.km: int = 0

    def __str__(self):
        return f"pass:{self.Pass}, gas:{self.gas}, km:{self.km}"

    