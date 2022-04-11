import db


class Order:
    def __init__(self, orderID):
        self.id = orderID
        self.completed = False


dbOrders = db.dbName["Orders"]
