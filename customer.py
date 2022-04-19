import db
dbCustomers = db.dbName["Customer"]
category = "Customer"


class Customer:
    def __init__(self, people):
        self.ordered = False
        self.people = people


def newCustomer():
    return {"user": "BaSic"}
