class Customers:
    def __init__(self, name, customer_ID):
        self.customer_ID = customer_ID
        self.name = name

    def get_customer_ID(self):
        return self.customer_ID

hash_table = [""] * 10

def hashvalue(ID):
    ID = int(ID)
    key = ID%5
    return key

def insert(nam, custard):
    global hash_table
    starting_index = hashvalue(custard)
    while hash_table[starting_index] != "":
        starting_index += 1
        if starting_index > 4:
            starting_index = 0
    hash_table[starting_index] = Customers(nam, custard)

def find_value(search_id):

    index = hashvalue(search_id)
    starting_index = index

    while hash_table[index] != "":

        if hash_table[index].get_customer_ID() == search_id:
            print("Value", search_id, "found at index", index)
            return

        index = (index + 1) % 5

        if index == starting_index:
            break

    print("Customer not found")


for i in range(4):
    a = input("Enter customer name: ")
    b = input("Enter customer ID: ")

    insert(a, b)

d = input("Enter the search thing: ")
find_value(d)

