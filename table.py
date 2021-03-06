import db
import random
dbTables = db.dbName["Tables"]


class Table:
    def __init__(self, Seats, **entries):
        self.Number = 0
        self.Seats = Seats
        self.Busy = False
        self.Ordered = False
        self.Clean = True
        self.__dict__.update(**entries)

    def showDetails(self):
        print(self.__dict__)

    def showNumber(self):
        return self.Number

    def cleanTable(self):
        self.Clean = True
        return self.Clean


def generateTables(n):
    instances = [Table(random.randrange(2, 8)) for i in range(n)]
    index = 1

    if(len(list(dbTables.find()))) > 0:
        return {"type": "error", "message": "Tables already exist!"}
    else:
        for i in instances:
            i.Number = index
            index += 1
            dbTables.insert_one(i.__dict__)
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
