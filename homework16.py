
# 1. დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, დაუწერეთ დეკორატორი, 
# რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი

def transaction_decorator(func):
    def wrapper(balance, amount_to_pay):
        commission = 1
        balance -= commission
        if balance < amount_to_pay:
            return "Error: Your balance is not sufficient to make payment"
        return func(balance, amount_to_pay)
    return wrapper

@transaction_decorator
def transaction(balance, amount_to_pay):
    balance -= amount_to_pay
    return f"Transaction successful, remaining balance: {balance}"

balance = 100
amount_to_pay = 50
print(transaction(balance, amount_to_pay))

amount_to_pay = 199
print(transaction(balance, amount_to_pay))

#  2. შექმენით მეტაკლასი, რომელიც სხვა კლასზე გამოყენების შემთხვევაში შეამოწმებს ამ კლასის მეთოდის სახელებს,
#    შემდეგი სახით: თუ მეთოდი იწყება _ ეს მეთოდი ვალიდური იქნება, თუ არ იწყება _, მაშინ აღზევდეს 
#    ValueError. მაგ: _test() - ეს მეთოდი იქნება ვალიდური, test() - ეს მეთოდი არ იქნება ვალიდური
#    და გამოიწვევს ValueError-ს. გაითვალისწინეთ რომ მეტაკლასმა უნდა შეამოწმოს მხოლოდ მეთოდები და არა ატრიბუტები!


class Metaclass(type):
    def __init__(cls, name, bases, class_dict):
        for method_name, method in class_dict.items():
            if not method_name.startswith('_') and callable(method):
                raise ValueError(f"'{method_name}' should start with an '_'.")
        super().__init__(name, bases, class_dict)

class MyClass(metaclass=Metaclass):
    def _valid_method(self):
        print("This method is valid.")
    
    def invalid_method(self):
        print("This method is invalid.")

try:
    obj = MyClass()
except ValueError as e:
    print(e)



