import db
import datetime
dbLogs = db.dbName["Logs"]


class Log:
    def __init__(self, who, what, when, category, type):
        self.who = who
        self.what = what
        self.when = when
        self.category = category
        self.type = type


def createLog(who, what, category, type):
    dbLogs.insert_one(Log(who, what, datetime.datetime.now(), category, type).__dict__)
    print(who, what, datetime.datetime.now())
