import db
import random
import gc
dbTables = db.dbName["Tables"]


class Table:
    def __init__(self, seats, **entries):
        self.Number = 0
        self.Seats = seats
        self.Busy = False
        self.Ordered = False
        self.Clean = True
        self.__dict__.update(**entries)

    def showDetails(self):
        print(self.Seats)

    def cleanTable(self):
        self.Clean = True


def generateTables(n):
    instances = [Table(random.randrange(2, 8)) for i in range(n)]
    index = 1

    if(len(list(dbTables.find()))) > 0:
        return "Tables already exist"
    else:
        for i in instances:
            i.Number = index
            index += 1
            dbTables.insert_one(i.__dict__)
        return f"{n} tables created!"


def getTablesToClean():
    tablesToClean = dbTables.find({'Clean': False})
    return tablesToClean
    # tablesToClean = dbTables.find_one({'clean': True})
    # x = Table(**tablesToClean)
    #
    # print(x.showDetails())
    # x = list(tablesToClean)
    # print(x)
    # Table(**x)
    # print(Table(x).__dict__)


def cleanTables(selectedTable):
    print(isinstance(selectedTable, Table))

    print(selectedTable)
    input()
    # for obj in gc.get_objects():
    #     if isinstance(obj, Table):
    #         print(obj.__dict__)
