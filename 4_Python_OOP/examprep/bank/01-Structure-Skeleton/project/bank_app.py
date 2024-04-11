from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self._get_client_by_id(client_id)
        loan = self._get_loan_by_type(loan_type)[0]

        if loan_type not in client.ALLOWED_LOANS:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self._get_client_by_id(client_id)

        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        target_loans = self._get_loan_by_type(loan_type)
        [loan.increase_interest_rate() for loan in target_loans]
        return f"Successfully changed {len(target_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        target_clients = self._get_client_by_rate(min_rate)
        [client.increase_clients_interest() for client in target_clients]
        return f"Number of clients affected: {len(target_clients)}."

    def get_statistics(self):
        total_income = sum(c.income for c in self.clients)
        granted_loans_count = sum([len(c.loans) for c in self.clients if c.loans])
        total_granted = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        total_not_granted = sum([loan.amount for loan in self.loans])
        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        return f"""Active Clients: {len(self.clients)}
Total Income: {total_income:.2f}
Granted Loans: {granted_loans_count}, Total Sum: {total_granted:.2f}
Available Loans: {len(self.loans)}, Total Sum: {total_not_granted:.2f}
Average Client Interest Rate: {avg_client_interest_rate:.2f}"""

    # helper methods
    def _get_client_by_id(self, client_id):
        selection = [c for c in self.clients if c.client_id == client_id]
        return selection[0] if selection else None

    def _get_loan_by_type(self, loan_type):
        return [loan for loan in self.loans if type(loan).__name__ == loan_type]

    def _get_client_by_rate(self, min_rate: float):
        selection = [c for c in self.clients if c.interest < min_rate]
        return selection
