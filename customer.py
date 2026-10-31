def add_customer(customers,plan,amount,start,end):
    name=input("Enter customer name:")
    email = input("Enter email:")
    for c in customers:
      if c["email"]==email: 
        print("Customer already exists")
        return
    customer={
        "id":len(customers)+1,
        "name":name,
        "email":email,
        "plan":plan,
        "amount":amount,
        "status":"active",
        "payment":"pending",
        "start_date":start,
        "end_date":end

    }  
    customers.append(customer)
    print("CUSTOMER ADDED SUCCESSFULLY!!!")
def view_customers(customers):
    if len(customers)==0:
        print("No customer found.")
        return
    for c in  customers:
        print("-------------------------")   
        print("ID:", c["id"])
        print("Name:", c["name"])
        print("email:", c["email"])
        print("Plan:", c["plan"])
        print("Amount:", c["amount"])
        print("Status:", c["status"])
def search_customer(customers):
    email = input("Enter email to search:")
    for c in customers:
        if c["email"] == email:
            print("CUSTOMER FOUND!!")
            print(c)
            return
    print("CUSTOMER NOT FOUND.")