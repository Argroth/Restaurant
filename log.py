import db
dbLogs = db.dbName["Logs"]

# example:
# who, category, action, result, date


def createLog(who, category, action, result, message, date):
    dbLogs.insert_one({
        "Who": who,
        "Category": category,
        "Action": action,
        "Result": result,
        "Message": message,
        "Date": date
    })
