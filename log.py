import db
dbCustomers = db.dbName["Log"]


class Log:
    def __init__(self, who, what, when):
        self.who = who
        self.what = what
        self.when = when


