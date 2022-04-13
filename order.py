import db
dbOrders = db.dbName["Orders"]


class Order:
    def __init__(self, orderID):
        self.id = orderID
        self.completed = False


def createOrder():
    dbOrders.insert_one({"order": "123"})

