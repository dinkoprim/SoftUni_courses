from project.clients.base_client import BaseClient


class Student(BaseClient):

    INTEREST = 2.0
    ALLOWED_LOANS = ["StudentLoan"]

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INTEREST)

    def increase_clients_interest(self):
        self.interest += 1.0

