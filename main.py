from tabulate import tabulate
import datetime

import log
import table
import customer
import staff
import order


# logs
# example:
# who, category, action, result, date
who = "system"
date = datetime.datetime.now()


# Menu
answer = True
update = ""
status = ""

while answer:
    print(f"""
    |                       Basic's Restaurant                          |
    |___________________________________________________________________|
    |    Customer options: | Staff options:  | Admin options:           |
    |    10. Enter         | 20. Guests      | 30. Generate Tables      |
    |    11. Order         | 21. Tables      | 31. Generate Staff       |
    |    12. Pay           | 22.             | 32. Generate Customers   |
    |    13. Leave         | 23.             | X.                       |
    |___________________________________________________________________|
    |                                                                   |
        Latest update: {update}                                         
    |___________________________________________________________________|
    |                                                                   |
        Current Status: {status}                                         
    |___________________________________________________________________|
    """)
    answer = input("Choose option: ")
    # Select main category
    if answer == "1":
        pass

    # Select Staff category
    elif answer == "21":
        category = "tables"
        tablesAnswer = input("""
            Choose option(staff):
                211. Clean Table
        """)

        # Get tables to clean and clean if needed
        if tablesAnswer == "211":
            action = "clean"
            tables = list(table.getTablesToClean())
            if (len(tables)) > 0:
                print(
                    tabulate(tables, headers="keys", tablefmt="fancy_grid")
                )

                # Select table to clean from list
                selectedTable = input("Select table to clean(by Number): ")

                # Clean selected table
                selectedTableObject = list(
                    filter(lambda tableObject: tableObject['Number'] == int(selectedTable), tables)
                )

                # Generate last update and create log
                feedback = (table.cleanTables(selectedTableObject))
                message = update = feedback["message"]
                log.createLog(who, category, action, feedback["type"], message, date)
            else:
                # Generate last update and create log
                message = update = "Nothing to clean! "
                result = "info"
                log.createLog(who, category, action, result, message, date)

    # Generate tables (number of tables)
    elif answer == "30":
        category = "tables"
        action = "generate"

        feedback = table.generateTables(int(input("Enter number of tables to generate: ")))
        if feedback["type"] == "success":
            update = feedback["message"]
            log.createLog(who, category, action, feedback["type"], feedback["message"], date)
        else:
            update = feedback["message"]
            log.createLog(who, category, action, feedback["type"], feedback["message"], date)

    elif answer == "9":
        pass

    elif answer == "Q" or answer == "q":
        print("\n Goodbye")
        answer = None

    elif answer == "x":

        update = customer.selectTable()
        # client = customer.newCustomer(4)
        # client.sitAtTable()
        # client.pay()
        # client.order()
        # update = client.__dict__

    elif answer == "logs":
        category = "user"
        action = "create"
        result = "Success"
        message = "test"
        log.createLog(who, category, action, result, message, date)

    else:
        print("\n Not Valid Choice Try again")

# TODO Create Receipt
# TODO Create Order queue
# TODO Create Staff
# TODO Create Tables
# TODO Create Customers
