from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next(filter(lambda c: c.id == customer_id, self.customers))

        try:
            rented_dvd = next(filter(lambda d: d.id == dvd_id, customer.rented_dvds))
            return f"{customer.name} has already rented {rented_dvd.name}"

        except StopIteration:
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd.is_rented:
            return f"DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = next(filter(lambda c: c.id == customer_id, self.customers))

        try:
            rented_dvd = next(filter(lambda d: d.id == dvd_id, customer.rented_dvds))
        except StopIteration:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(rented_dvd)
        rented_dvd.is_rented = False
        return f"{customer.name} has successfully returned {rented_dvd.name}"

    def __repr__(self):
        return '\n'.join([
            *[str(c) for c in self.customers],
            *[str(d) for d in self.dvds],
        ])

        # result = ''
        # for customer in self.customers:
        #     result += f'{customer}' + '\n'
        # for dvd in self.dvds:
        #     result += f'{dvd}' + '\n'
        # return result.rstrip()






