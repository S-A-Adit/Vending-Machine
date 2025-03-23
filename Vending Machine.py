def display_products():
    products = {110: 'Soda', 111: 'Chocolate Milk', 112: 'Water', 113: 'Coffee', 114: 'Candy', 115: 'Chips', 116: 'Cookies', 117: 'Chocolate Bar'}
    price = (2.45, 3.85, 3.35, 4.95, 1.55, 2.85, 1.95, 5.65)
    print("Products available for purchase:")
    for item in products:
        print(item, ":", products[item], "worth $", price[item - 110])
    return products, price


def calculate_change(input_money, purchased_amount):
    change = input_money - purchased_amount
    return change


def update_inventory(inventory, quantity):
    remaining_product_quantity = inventory - quantity
    return remaining_product_quantity

def calc_purchase(price,quantity):
    total_pay = price * quantity
    return total_pay


def main():
    inventory = {'Soda': 30, 'Chocolate Milk': 30, 'Water': 30, 'Coffee': 30, 'Candy': 30, 'Chips': 30, 'Cookies': 30, 'Chocolate Bar': 30}
    ask_user = 'y'
    while ask_user == 'y':
        print("Welcome! To buy choose from the following numbers:")
        products, price = display_products()
        product_code = int(input("Enter product number: "))
        while product_code not in products:
            print("Error! Input Code from 110 to 117 only")
            product_code = int(input("Enter product number: "))
        print("Your selected product is", products[product_code], "With Unit Price of $", price[product_code-110])
        quantity = int(input("What quantity do you want for the product: "))
        while quantity < 0 or quantity > inventory[products[product_code]]:
            print("Inventory is out or wrong value for the inventory!")
            quantity = int(input("What quantity do you want for the product: "))
        inventory[products[product_code]] -= quantity
        purchase_value = 0.0 + calc_purchase(price[product_code-110], quantity)
        print("The item",  products[product_code], "is available in the following quantity", inventory[products[product_code]])
        for item, quantity in inventory.items():
            if quantity == 0:
                inventory[item] = 30
        ask_user = input("Do you want to buy anything else? Enter y to continue purchasing:").lower()

    print("Do you want to pay in cash or card?")
    payment_method = input("Enter either cash or card only:").lower()
    while payment_method != 'card' and payment_method != 'cash':
        print("Choose proper paying method")
        payment_method = input("Enter either cash or card only:").lower()
    print(purchase_value)
    if payment_method == 'cash':
        payment = float(input("Enter payment value: "))
        print("Your change is",calculate_change(payment, purchase_value))
    else:
         print("Your purchased amount is", purchase_value)


if __name__ == "__main__":
    main()