from typing import List

from project.animal import Animal
from project.worker import Worker


def type_finder(objects_list, searched_type):
    result = [item for item in objects_list if item.__class__.__name__ == searched_type]
    return result


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) < self.__animal_capacity and self.__budget > price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return f"Not enough budget"

        return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return f"Not enough space for worker"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker.name} fired successfully"

    def pay_workers(self):
        workers_cost = sum([w.salary for w in self.workers])

        if workers_cost <= self.__budget:
            self.__budget -= workers_cost
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_cost = sum([a.money_for_care for a in self.animals])

        if animals_cost <= self.__budget:
            self.__budget -= animals_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals'

        lions = type_finder(self.animals, 'Lion')
        amount_of_lions = len(lions)

        tigers = type_finder(self.animals, 'Tiger')
        amount_of_tiger = len(tigers)

        cheetahs = type_finder(self.animals, 'Cheetah')
        amount_of_cheetah = len(cheetahs)

        result += f'\n----- {amount_of_lions} Lions:'
        for lion in lions:
            result += f'\n{lion}'

        result += f'\n----- {amount_of_tiger} Tigers:'
        for tiger in tigers:
            result += f'\n{tiger}'

        result += f'\n----- {amount_of_cheetah} Cheetahs:'
        for cheetah in cheetahs:
            result += f'\n{cheetah}'

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"

        keepers = type_finder(self.workers, 'Keeper')
        amount_of_keepers = len(keepers)

        caretakers = type_finder(self.workers, 'Caretaker')
        amount_of_caretakers = len(caretakers)

        vets = type_finder(self.workers, 'Vet')
        amount_of_vets = len(vets)

        result += f'\n----- {amount_of_keepers} Keepers:'
        for keeper in keepers:
            result += f'\n{keeper}'

        result += f'\n----- {amount_of_caretakers} Caretakers:'
        for taker in caretakers:
            result += f'\n{taker}'

        result += f'\n----- {amount_of_vets} Vets:'
        for vet in vets:
            result += f'\n{vet}'

        return result



