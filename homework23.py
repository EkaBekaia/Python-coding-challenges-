# 1. მოცემულია ფუქცია, რომელიც პარამეტრად იღებს order-ების ლისტს,
#    order-ები არის დიქტების სახით: {"product": "apple, "quantity": 5}
#    inventory არის დიქტის სახით: {"product": stock}

#    ფუნქცია ამოწმებს ორდერში მოთხოვნილი პროდუქტი თუ არის inventory-ში, ამოწმებს თუ არის საკმარისი
#    ოდენობა და შემდეგ inventory-ში აკლებს მოთხოვნილ ოდენობას და successful_orders-ში ამატებს order-ს.

#    def process_orders(orders, inventory):

#     successful_orders = []

#     for order in orders:
#         product = order["product"]
#         quantity = order["quantity"]

#         if product not in inventory:
#             raise ValueError(f"Product '{product}' not found in inventory")

#         if quantity > inventory[product]:
#             raise ValueError(f"Not enough stock for '{product}'")

#         inventory[product] -= quantity
#         successful_orders.append(order)

#     return successful_orders

# ამ ფუნქციისთვის დაწერეთ ტესტი, რომელიც შეამოწმებს 
#    ა. order-ში გადმოცემული პროდუქტი არის თუ არა საწყობში
#    ბ. order-ში გადმოცემული პროდუქტის ოდენობა არის თუ არა საწყობში
#    გ. თუ ყველაფერი სწორად გადმოეცა, საბოლოოდ სწორად აკლებს თუ არა საწყობში არსებული
#       პროდუქტის ოდენობას order-ში მოთხოვნილ ოდენობას

# ტესტის ფაილი შექმენით ცალკე!


import unittest

from main_file import process_orders  

class TestProcessOrders(unittest.TestCase):

    def setUp(self):
        
        self.inventory = {
            "apple": 10,
            "banana": 5,
            "orange": 7
        }

    def test_product_not_found_in_inventory(self):    
        orders = [{"product": "grape", "quantity": 3}]
        with self.assertRaises(ValueError) as context:
            process_orders(orders, self.inventory)
        self.assertEqual(str(context.exception), "Product 'grape' not found in inventory")

    def test_not_enough_stock(self):      
        orders = [{"product": "apple", "quantity": 15}]
        with self.assertRaises(ValueError) as context:
            process_orders(orders, self.inventory)
        self.assertEqual(str(context.exception), "Not enough stock for 'apple'")

    def test_successful_order_processing(self):       
        orders = [{"product": "apple", "quantity": 5}]
        successful_orders = process_orders(orders, self.inventory)
        
        #successfull orders added
        self.assertEqual(len(successful_orders), 1)
        self.assertEqual(successful_orders[0], {"product": "apple", "quantity": 5})
        
        # remaning items in stock
        self.assertEqual(self.inventory["apple"], 5)

    def test_multiple_successful_orders(self):        
        orders = [
            {"product": "apple", "quantity": 5},
            {"product": "banana", "quantity": 3},
            {"product": "orange", "quantity": 5}
        ]
        successful_orders = process_orders(orders, self.inventory)
       
        self.assertEqual(len(successful_orders), 3)        
       
        self.assertEqual(self.inventory["apple"], 5)
        self.assertEqual(self.inventory["banana"], 2)
        self.assertEqual(self.inventory["orange"], 2)

if __name__ == "__main__":
    unittest.main()
