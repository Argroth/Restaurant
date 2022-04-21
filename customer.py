import db
import gc
from tabulate import tabulate
import table

dbCustomers = db.dbName["Customer"]
category = "Customer"


class Customer:
    def __init__(self, people):
        self.People = people
        self.Ordered = False
        self.Paid = False
        self.TableOccupied = ""

    def order(self):
        self.Ordered = True

    def pay(self):
        self.Paid = True

    def sitAtTable(self, tableToSit):
        self.TableOccupied = tableToSit


def newCustomer(people):
    customer = Customer(people)
    return customer


def checkForFreeTable():
    freeTables = []
    for obj in gc.get_objects():
        if isinstance(obj, table.Table):
            tableToCheck = obj.__dict__
            if not tableToCheck["Busy"]:
                freeTables.append(obj)

    return freeTables


def selectTable(clientObj):
    freeTables = checkForFreeTable()
    freeTablesToChoose = []
    client = clientObj.__dict__
    for tableObj in freeTables:
        if client["People"] <= tableObj.Seats:
            freeTablesToChoose.append(tableObj.notBusy())
    print(
        tabulate(freeTablesToChoose, headers="keys", tablefmt="fancy_grid")
    )
    print(client)
    selectedTable = input("Select table  to sit: ")
    clientObj.sitAtTable(selectedTable)
    print(clientObj.__dict__)
    return "x"


def order():
    return "Ordering"


def leave():

    return "Leaving"
