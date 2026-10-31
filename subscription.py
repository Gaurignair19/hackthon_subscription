from datetime import date,timedelta
def display_plans():
    print("\n---SUBSCRIPTION PLANS ---")
    print("1.SILVER-$199")
    print("2.GOLD-$399")
    print("3.PLATINUM-$599")
def choose_plan():
    display_plans
    choice=input("choose tour plan:")
    if choice=="1":
        plan ="SILVER"
        amount =199
    elif choice=="2":
        plan ="GOLD"
        amount =399
    elif choice=="3":
         plan ="PLATINUM"
         amount =599
    else: 
         print("invalid choice!!")
         return None 
    start =date.today()
    end=start+timedelta(days=30)
    print("Plan selected:",plan)
    print("Amount:$",amount)
    print("start date:",start)
    print("End date:",end)
    return plan,amount,str(start),str(end)