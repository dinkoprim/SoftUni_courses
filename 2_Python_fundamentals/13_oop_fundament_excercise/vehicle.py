class Vehicle:
	def __init__(self, type: str, model: str, price: int, owner=None):
		self.type = type
		self.model = model
		self.price = price
		self.owner = owner
		
	def buy(self, money: int, owner: str):
		if not self.owner:
			if money >= self.price:
				self.owner = owner
				money -= self.price
				return f"Successfully bought a {self.type}. Change: {money:.2f}"
			else:
				return f"Sorry, not enough money"
		else:
			return f"Car already sold"

	def sell(self):
		if self.owner:
			self.owner = None
		else:
			return f"Vehicle has no owner"

	def __repr__(self):
		if self.owner:
			return f"{self.model} {self.type} is owned by: {self.owner}"
		else:
			return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
