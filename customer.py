import db


class Customer:
    def __init__(self, people):
        self.ordered = False
        self.people = people


dbCustomers = db.dbName["Customer"]
