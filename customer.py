import db
dbCustomers = db.dbName["Customer"]


class Customer:
    def __init__(self, people):
        self.ordered = False
        self.people = people


