class Catalogue:

	def __init__(self, name: str):
		self.name = name
		self.products = []

	def add_product(self, product_name: str):
		self.products.append(product_name)

	def get_by_letter(self, first_letter: str):
		# by_first_letter = []
		# for product in self.products:
		# 	if product[0] == first_letter:
		# 		by_first_letter.append(product)
		# return by_first_letter
		return [product for product in self.products if product.startswith(first_letter)]

	def __repr__(self):
		sorted_products = sorted(self.products)
		each_product_new_line = '\n'.join(sorted_products)
		return f"Items in the {self.name} catalogue:\n{each_product_new_line}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
