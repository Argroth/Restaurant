import db
import table
import staff
import order
import customer
from dotenv import load_dotenv
import gc

# table1 = table.Table(4)
# person1 = customer.Customer(4)
# order1 = order.Order(1)
# staff1 = staff.Person()

# print(table1.__dict__)
# print(person1.__dict__)
# print(order1.__dict__)
# print(staff1.__dict__)

# table.dbTables.insert_one(table1.__dict__)

selectedTable = table.dbTables.find_one({})
x = table.Table(**selectedTable)

print(x.showDetails())

answer = True
while answer:
    print(f"""
        Customer options:
        1.
        2.
        3.
        -----------
        Staff options:
        4. Serve
        5. Check Tables
        6.
    """)
    answer = input("Choose option: ")
    if answer == "1":
        pass
    elif answer == "2":
        pass
    elif answer == "3":
        pass
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
