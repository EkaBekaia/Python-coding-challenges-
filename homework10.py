# 1. გამოიყენეთ lambda ფუნქცია sorted() ფუნქციაში, იმისათვის რომ დაასორტიროს მოცემული ლისტი:
#    [(1, 3), (4, 2), (2, 5)] - მასში არსებული ელემენტების მეორე ელემენტის მიხედვით



list= [(1, 3), (4, 2), (2, 5)]
sorted_list = sorted(list, key=lambda x: x[1])
print(sorted_list)


# # 2. დაწერეთ ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ორ რიცხვს და პირველ რიცხვს გაყოფს მეორე რიცხვზე და დააბრუნებს შედეგს, 
# # დაიჭირეთ ორი ერორი: ის რომ მომხმარებელმა ინტეჯერები შეიყვანოს და ნულზე რომ არ შეიძლება გაყოფა, თითოეული ერორისთვის გამოუტანეთ 
# # შესაბამისი შეტყობინება. (ორივე ერორი უნდა იყოს შესაბამისი ერორებით დაჭერილი, არ გამოიყენოთ ზოგადი იქსეფშენი)


def divide_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))  # Fixed typo in prompt
        result = num1 / num2
        print(f"Result is: {result}")
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("You cannot divide by 0!")

divide_numbers()

# # 3. მოცემულია პროდუქტების ლისტი:

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

# filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
# map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
# sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
# reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი



low_price_products = filter(lambda p: p["price"] < 100, products)
for product in low_price_products:
    print(product)

product_names_prices = map(lambda p: f'{p["name"]}: {p["price"]}', products)
for item in product_names_prices:
    print(item)

sorted_products = sorted(products, key=lambda p: p["price"])
for product in sorted_products:
    print(product)

from functools import reduce
total_price = reduce(lambda sum, p: sum + p["price"], products, 0)
print(total_price)