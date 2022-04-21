import db
import random
dbTables = db.dbName["TablesArchive"]


class Table:
    def __init__(self, Seats, Number, **entries):
        self.Number = Number
        self.Seats = Seats
        self.Busy = False
        self.Ordered = False
        self.Clean = True
        self.__dict__.update(**entries)

    def showDetails(self):
        print(self.__dict__)

    def showNumber(self):
        return self.Number

    def notBusy(self):
        return {"Number": self.Number, "Busy": self.Busy, "Seats": self.Seats}

    def cleanTable(self):
        self.Clean = True
        return self.Clean


tablesInstances = []


def generateTables(n):
    tablesInstances.append([Table(random.randrange(2, 8), i) for i in range(n)])

    if(len(tablesInstances)) > 0:
        return {"type": "error", "message": "Tables already exist!"}
    else:
        return {"type": "success", "message": f"{n} tables created"}


def getTablesToClean():
    tablesToClean = dbTables.find({'Clean': False})
    return tablesToClean


def cleanTables(selectedTable):
    selectedTableDict = selectedTable[0]
    tableObj = Table(**selectedTableDict)

    tableObj.cleanTable()
    dbTables.find_one_and_update({
        "Number": tableObj.showNumber()}, {"$set": {"Clean": tableObj.cleanTable()}}
    )

    return {"type": "success", "message": f"Table {selectedTableDict['Number']} cleaned!"}
