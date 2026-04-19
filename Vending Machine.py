import csv
from datetime import datetime

# Snack Details
Snack_ID = [43, 45, 46, 48, 53, 55]
Snack_Name = ["Kinder Bruno\t   ", "Highway Cake\t   ", "Slai O'lai\t       ", "Biskrem\t       ", "Snickers\t       ", "Chocolate Sando   "]
Snack_Quantity = [15, 15, 15, 15, 15, 15]
Snack_Cost = [50, 25, 15, 25, 40, 15]

# Drink Details
Drink_ID = [13, 14, 16, 21, 33, 35]
Drink_Name = ["Pearona\t           ", "Appletiser\t           ", "Fanta Grape\t       ", "Coca Cola\t           ", "Mirinda Raspberry\t   ", "Fuze Tea Peach\t       "]
Drink_Quantity = [10, 10, 10, 10, 10, 10]
Drink_Cost = [60, 75, 55, 65, 45, 65]
ids = Snack_ID + Drink_ID

# Display Snacks
def show_snacks():
    print("\nSnacks:")
    print("ID   Name                Cost      Quantity")
    for i in range(len(Snack_ID)):
        print(Snack_ID[i], " ", Snack_Name[i], " Rs", str(Snack_Cost[i]), "      ", Snack_Quantity[i])

# Display Drinks
def show_drinks():
    print("\nDrinks:")
    print("ID   Name                    Cost       Quantity")
    for i in range(len(Drink_ID)):
        print(Drink_ID[i], " ", Drink_Name[i], " Rs", str(Drink_Cost[i]), "      ", Drink_Quantity[i])

# Transaction Log
def log_transaction(category, product_name, product_id, cost, money_inserted, change, quantity):
    with open("transactions.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), category, product_name, product_id, cost, money_inserted,
             change, quantity])

# Main Program
def vending_machine():
    print("\nWelcome to PolyTechnic's Vending Machine!")
    current_balance = 0
# Selection
    while True:
        print(f"\nCurrent balance: Rs{current_balance}")
        print("\nChoose category to continue transaction:")
        print("1 - Snacks")
        print("2 - Drinks")
        print("0 - Exit (Refund balance)")
        choice = input("Your choice: ")
# Selection Verification
        if choice == '0':
            if current_balance > 0:
                print(f"Refunding your balance of Rs{current_balance}")
            print("Hope to see you again!")
            break
        elif choice == '1':
            show_snacks()
            category = "Snack"
        elif choice == '2':
            show_drinks()
            category = "Drink"
        else:
            print("Invalid category choice. Try again.")
            continue

# Only ask for money if current balance is zero
        if current_balance == 0:
            Accept_Money = [1, 5, 10, 20, 25, 50, 100, 200]
            money_input = input("Insert money (RS): ")
            if money_input == '1' or money_input == '5' or money_input == '10' or money_input == '20' or money_input == '25' or money_input == '50' or money_input == '100' or money_input == '200':
                money = int(money_input)
                current_balance += money
                print(f"Inserted money amount: Rs{money}. Current balance: Rs{current_balance}")
            else:
                print("Invalid money amount. Try again.")
                continue

# Product validation
        prod_id_input = input("Insert product ID: ")
        if (prod_id_input == '43' or prod_id_input == '45' or prod_id_input == '46' or prod_id_input == '48' or
                prod_id_input == '53' or prod_id_input == '55' or prod_id_input == '13' or prod_id_input == '14' or
                prod_id_input == '16' or prod_id_input == '21' or prod_id_input == '33' or prod_id_input == '35'):
            prod_id = int(prod_id_input)
            print("Selected ID:", prod_id)
        else:
            print("Invalid ID. Try again.")
            continue

# Process selection
        if prod_id in Snack_ID:
            idx = Snack_ID.index(prod_id)
            cost = Snack_Cost[idx]
            qty = Snack_Quantity[idx]
            name = Snack_Name[idx]
            product_quantities = Snack_Quantity
        elif prod_id in Drink_ID:
            idx = Drink_ID.index(prod_id)
            cost = Drink_Cost[idx]
            qty = Drink_Quantity[idx]
            name = Drink_Name[idx]
            product_quantities = Drink_Quantity
        else:
            print("Invalid product ID.")
            continue

        if qty <= 0:
            print(f"{name} is out of stock.")
            continue

        # Quantity selection
        # Quantity selection
        while True:
            quantity_input = input(f"Enter quantity (available: {qty}): ")
            if quantity_input == "":
                print("Please enter a number.")
            elif quantity_input in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]:
                quantity = int(quantity_input)
                if quantity > qty:
                    print(f"Not enough stock. Only {qty} available.")
                else:
                    break
            else:
                print("Please enter a number between 1-9.")

        total_cost = cost * quantity

        if current_balance < total_cost:
            print(f"Not enough money. {quantity} {name.strip()} costs Rs{total_cost}. Current balance: Rs{current_balance}")
            continue

        product_quantities[idx] -= quantity
        current_balance -= total_cost
        print(f"\nDispensing {quantity} {name.strip()}. Remaining balance: Rs{current_balance}")
        log_transaction(category, name.strip(), prod_id, total_cost, current_balance + total_cost, current_balance, quantity)

# Ask if user wants to make another purchase
        another = input("Would you like to make another purchase? (yes/no): ").lower()
        if another != 'yes':
            if current_balance > 0:
                print(f"Refunding your balance of Rs{current_balance}")
            print("Thank you for your purchase! Hope to see you again!")
            break
vending_machine()