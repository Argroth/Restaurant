import db
dbCustomers = db.dbName["Customer"]
category = "Customer"


class Customer:
    def __init__(self, people):
        self.people = people
        self.ordered = False
        self.paid = False
        self.tableOccupied = ""

    def order(self):
        self.ordered = True

    def pay(self):
        self.paid = True

    def sitAtTable(self):
        self.tableOccupied = 2


def newCustomer(people):
    customer = Customer(people)
    return customer
