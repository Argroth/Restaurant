import db


class Person:
    def __init__(self):
        self.busy = False


class Chef(Person):
    role = "Chef"


class Waiter(Person):
    role = "Waiter"


dbStaff = db.dbName["Staff"]
