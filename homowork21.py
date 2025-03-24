
# დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და შეამოწმებს ეს რიცხვი არის თუ არა მარტივი

# შემდეგ ნაკადების გამოყენებით გაუშვით ეს ფუნქცია პარალელურად რომ შეამოწმოს შემდეგ ლისტში
# num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51] ყველა რიცხვი და დააბრუნოს პასუხი


import concurrent.futures

num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

def check_if_simple(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def parallel_check(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
         results = list(executor.map(check_if_simple, numbers))

    result_dict = {}
    for i, num in enumerate(numbers):
        result_dict[num] = results[i]
    
    return result_dict


result = parallel_check(num_list)
print(result)
