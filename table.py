import db


class Table:
    def __init__(self, seats, **entries):
        self.seats = seats
        self.busy = False
        self.ordered = False
        self.clean = True
        self.__dict__.update(**entries)

    def showDetails(self):
        print(self.seats)


dbTables = db.dbName["Tables"]
