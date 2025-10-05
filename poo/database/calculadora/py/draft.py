class Calculadora:
	def __init__(self, batteryMax: int):
		self.display = 0.0
		self.battery = 0
		self.batteryMax = batteryMax

	def __str__(self):
		return f"display = {self.display:.2f}, battery = {self.battery}"

	def charge(self, increment: int):
		self.battery += increment
		if self.battery > self.batteryMax:
			self.battery = self.batteryMax

	def useBattery(self) -> bool:
		if self.battery <= 0:
			print('fail: bateria insuficiente')
			return False
		self.battery -= 1
		return True

	def sum(self, a: float, b: float):
		if not self.useBattery():
			return
		self.display = a + b

	def div(self, num: float, den: float):
		if not self.useBattery():
			return
		if den == 0:
			print("fail: divisao por zero")
			return
		self.display = num / den

def main():
	calc = None
	while True:
		line = input()
		print("$" + line)
		args = line.split()
		if args[0] == "end":
			break
		elif args[0] == "init":
			calc = Calculadora(int(args[1]))
		elif args[0] == "charge":
			if calc:
				calc.charge(int(args[1]))
			else:
				print("fail: calculadora nao inicializada")
		elif args[0] == "sum":
			if calc:
				calc.sum(float(args[1]), float(args[2]))
			else:
				print("fail: calculadora nao inicializada")
		elif args[0] == "div":
			if calc:
				calc.div(float(args[1]), float(args[2]))
			else:
				print("fail: calculadora nao inicializada")
		elif args[0] == "show":
			if calc:
				print(calc)
			else:
				print("fail: calculadora nao inicializada")

main()
