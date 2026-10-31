from datetime import date,timedelta
def renew_subscritiption(customers):
    email=input("Enter Customer email:")
    for c in customers:
        if c[email]==email:
            if c["status"]=="cancelled":
                print("subsription is CANCELLED!")
                return
            old_date=date.fromisoformat(c["end_date"])
            new_date=max(old_date,date.today())+timedelta(days=30)
            c["end_date"]=str(new_date)
            c["satus"]="Active"
            print("SUBSCRIPTION RENEWED SUCCESSFULLY!!!")
            print("New Expiry date:",new_date)
            return
        print("Customer not found!")
def cancel_subscritiption(customers):
    email=input("Enter customer email:") 
    for c in customers:
        if c["email"]==email:
            c["status"]="cancelled"
            print("subscription CANCELLED successfully!!!")
            return
    print("Customer not found!")
def check_expired(customers):
    today=date.today()
    print("\n----EXPIRED SUBSCRIPTION----")
    found=False
    for c in customers:
      if c["status"]=="Active":
        end_date=date.fromisoformat(c["end_date"])
        if end_date<today:
            c["status"]="Expired"
            print(c["name"],"-",c["email"])
            found=True
    if found==False:
        print("No expired subscriptions found")

         