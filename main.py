import db
import gc

from tabulate import tabulate
from dotenv import load_dotenv

import table
import staff
import order
import customer

# selectedTable = table.dbTables.find_one({})
# x = table.Table(**selectedTable)
#
# print(x.showDetails())
answer = True
update = ""
status = ""


class Status:
    def __init__(self):
        self.currentStatus = None

    def createNewStatus(self, statusToCreate):
        self.currentStatus = statusToCreate


while answer:
    print(f"""
    |                       Basic's Restaurant                          |
    |___________________________________________________________________|
    |    Customer options: | Staff options:  | Admin options:           |
    |    10. Enter         | 20.             | 30. Generate Tables      |
    |    11.               | 21.             | 31. Generate Staff       |
    |    12.               | 22.             | 32. Generate Customers   |
    |    13.               | 23.             | X.                       |
    |___________________________________________________________________|
    |                                                                   |
        Latest update: {update}                                         
    |___________________________________________________________________|
    |                                                                   |
        Current Status: {status}                                         
    |___________________________________________________________________|
    """)
    answer = input("Choose option: ")
    if answer == "1":
        pass
    elif answer == "2":
        pass
    # Get tables to clean and clean if needed
    elif answer == "x":
        tables = list(table.getTablesToClean())
        if (len(tables)) > 0:
            print(
                tabulate(tables, headers="keys", tablefmt="fancy_grid")
            )

            selectedTable = input("Select table to clean(by Number): ")
            selectedTableObject = list(filter(lambda tableObject: tableObject['Number'] == int(selectedTable), tables))

            update = (table.cleanTables(selectedTableObject))
        else:
            update = "Nothing to clean! "
    # Generate tables (number of tables)
    elif answer == "10":
        print(
            table.generateTables(int(input("Enter number of tables to generate: ")))
        )
    elif answer == "9":
        pass
    elif answer == "Q" or answer == "q":
        print("\n Goodbye")
        answer = None
    else:
        print("\n Not Valid Choice Try again")

# TODO Create Receipt
# TODO Create Order queue
# TODO Create Staff
# TODO Create Tables
# TODO Create Customers
