class Inventory:
	__capacity = 0

	def __init__(self, capacity: int):
		self.capacity = capacity
		Inventory.__capacity = self.capacity
		self.items = []
		self.left_capacity = Inventory.__capacity

	def add_item(self, item: str):
		if Inventory.__capacity > len(self.items):
			self.items.append(item)
			self.left_capacity -= 1
		else:
			return f"not enough room in the inventory"

	def get_capacity(self):
		return Inventory.__capacity

	def __repr__(self):
		return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
