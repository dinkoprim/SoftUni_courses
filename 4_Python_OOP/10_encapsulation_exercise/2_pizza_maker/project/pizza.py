from typing import Dict

from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[Topping.topping_type: Topping.weight] = {}

        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, proper_string):
        if not proper_string:
            raise ValueError("The name cannot be an empty string")
        self.__name = proper_string
        
    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.__max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        self.toppings[topping.topping_type] = self.toppings.get(topping.topping_type, 0) + topping.weight

    def calculate_total_weight(self):
        pizza_weight = sum(self.toppings.values()) + self.dough.weight
        return pizza_weight




