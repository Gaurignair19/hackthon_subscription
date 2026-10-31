
import json
import os
import customer
import subscription
import payment
import renewal
if os.path.exists("data.json"):
    with open("data.json", "r") as file:
        customers = json.load(file)
else:
    customers = []

while True:
    print("\n===== SUBSCRIPTION MANAGEMENT SYSTEM =====")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. View Subscription Plans")
    print("5. Update Payment")
    print("6. View Payments")
    print("7. Calculate Revenue")
    print("8. Renew Subscription")
    print("9. Cancel Subscription")
    print("10. Check Expired Subscriptions")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = subscription.choose_plan()

        if result is not None:
            plan, amount, start, end = result
            customer.add_customer(customers, plan, amount, start, end)

    elif choice == "2":
        customer.view_customers(customers)

    elif choice == "3":
        customer.search_customer(customers)

    elif choice == "4":
        subscription.display_plans()

    elif choice == "5":
        payment.update_payment(customers)

    elif choice == "6":
        payment.view_payments(customers)

    elif choice == "7":
        payment.calculate_revenue(customers)

    elif choice == "8":
        renewal.renew_subscription(customers)

    elif choice == "9":
        renewal.cancel_subscription(customers)

    elif choice == "10":
        renewal.check_expired(customers)

    elif choice == "11":
        with open("data.json", "w") as file:
            json.dump(customers, file, indent=4)

        print("Data saved successfully!")
        print("Thank you for using our system!")
        break

    else:
        print("Invalid choice! Try again.")
    with open("data.json", "w") as file:
        json.dump(customers, file, indent=4)
