import db
dbLogs = db.dbName["Logs"]

# example:
# who, category, action, result, date


def createLog(who, category, action, result, date):
    print(who, category, action, result, date)
