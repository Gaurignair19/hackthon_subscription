def update_payment(customers):
    email=input("Enter customer email:")
    for c in customers:
        if c["email"]==email:
            print("1.Paid")
            print("2.Pending")
            choice=input("Enter payment status")
            if choice=="1":
                c["payment"]="paid"
                print("PAYMENT UPDATED SUCCESFULLY!!")
            elif choice=="2":
                c["payment"]="pending"
                print("PAYMENT MARKED AS PRNDING")
            else:
                print("Invalid Choice!!")
            return
    print("Customer not found!!")
def view_payments(customers):
    if len(customers)==0:
        print("No customer record found.")
        return
    for c in customers:
        print("----------------------")
        print("Name:",c["name"])
        print("Email:",c["email"])
        print("Amount:",c["amount"])
        print("Payment:",c["payment"])
def calculate_revenue(customers):
    total=0
    for c in customers:
        if c["payment"]=="paid":
            total=total+c["amount"]
    print("Total Revenue $",total)
