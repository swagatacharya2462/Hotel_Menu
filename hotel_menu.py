menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

print("Welcome to Swagat's Restaurant")
for key, value in menu.items():
    print(f"{key}: Rs {value}")

order_total = 0

while True:
    item = input("Enter the name of the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available!")

    another_order = input("Do you want to add another item? (Yes/No): ")
    if another_order.lower() != "yes":
        break

print(f"The total amount of items to pay is Rs {order_total}")

# Customer satisfaction rating
try:
    rating = int(input("Please rate your experience from 1 to 5: "))
    if rating == 5:
        print("Thank you! We're glad you loved your experience at Swag's Restaurant!")
    elif rating == 4:
        print("Thank you! We're happy you enjoyed your visit!")
    elif rating == 3:
        print("Thank you for your feedback! We'll work to improve.")
    elif rating == 2:
        print("We're sorry to hear that. We'll strive to do better.")
    elif rating == 1:
        print("We apologize for the inconvenience. Your feedback will help us improve.")
    else:
        print("Invalid rating! Please provide a rating between 1 and 5.")
except ValueError:
    print("Invalid input! Please enter a number between 1 and 5.")

print("Thank you for visiting Swag's Restaurant!")
