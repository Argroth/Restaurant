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
while answer:
    print(f"""
        Customer options:
        1. Enters
        2.
        3.
        -----------
        Staff options:
        4. 
        5. 
        6.
        7.
        -----------
        Admin options:
        10. Generate tables
        11. Generate Staff
    """)
    answer = input("Choose option: ")
    if answer == "1":
        pass
    elif answer == "2":
        pass
    elif answer == "3":
        pass
    # Get tables to clean and clean if needed
    elif answer == "4":
        tables = list(table.getTablesToClean())
        if (len(tables)) > 0:
            print(
                tabulate(tables, headers="keys", tablefmt="fancy_grid")
            )

            selectedTable = input("Select table to clean(by Number): ")
            selectedTableObject = list(filter(lambda tableObject: tableObject['Number'] == int(selectedTable), tables))

            table.cleanTables(selectedTableObject)
        else:
            print("Nothing to clean! ")
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

# TODO Create DB Connection
# TODO Create Receipt
# TODO Clean tables after customer
# TODO Create Order queue
# TODO Create Staff
# TODO Create Tables
# TODO Create Customers
