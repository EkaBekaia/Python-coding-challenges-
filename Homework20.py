# თქვენი დავალებაა დაწეროთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და გადაცემული რიცხვის საფუძველზე 
# იმდენჯერ ჰკითხავს მომხმარებელს სახელს და ასაკს, შემდეგ კი persons.json ფაილში დაამატებს ახალ პერსონებს
# თავისივე აიდებით.მაგალითათ ორჯერ ვეკითხებით მომხმარებელს:

# enter your name: Walter
# enter your age: 45
# enter your name: Niko
# enter your age: 32

# persons.json უნდა გამოიყურებოდეს შემდეგნაირად:

# [
#     {
#         "id": 1,
#         "name": "Ana",
#         "age": 19
#     },
#     {
#         "id": 2,
#         "name": "Bob",
#         "age": 21
#     },
#     {
#         "id": 3,
#         "name": "Walter",
#         "age": 45
#     },
#     {
#         "id": 4,
#         "name": "Niko",
#         "age": 32
#     }
# ]

# გაითვალისწინეთ! არ უნდა დაირღვეს json ფაილის სტრუქტურა, ანუ პერსონები უნდა იყოს ლისტში, ლისტის გარეთ არ ჩაამატოთ!
# ასევე, აიდები უნდა გაგრძელდეს ბოლო აიდის მქონე პერსონის შემდეგ ლოგიკურად, ანუ json ფაილში თუ ბოლო პერსონის აიდი იქნება 2, 
# ახალი პერსონის დამატებისას აიდი უნდა იყოს 3, თუ ბოლო პერსონის აიდი იქნება 5, ახალი პერსონის უნდა იყოს 6 და ასე შემდეგ!  და ცალკე მაქვს ფაილი persons სადაც წერია [
#     {
#         "id": 1,
#         "name": "Ana",
#         "age": 19
#     },
#     {
#         "id": 2,
#         "name": "Bob",
#         "age": 21
#     }
# ]





import json

def add_persons_to_json(count):
    try:
        with open('persons_list.json', 'r') as file:
            persons = json.load(file)
    except FileNotFoundError:
        persons = []

    if persons:
        last_id = persons[-1]["id"]
    else:
        last_id = 0

    for _ in range(count):
        name = input("Enter your name: ")

        while True:
            try:
                age = int(input("Enter your age: "))
                if age <= 0:
                    print("Please enter a valid age greater than 0.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number for age.")

        new_person = {
            "id": last_id + 1,
            "name": name,
            "age": age
        }

        persons.append(new_person)
        last_id += 1

    with open('persons_list.json', 'w') as file:
        json.dump(persons, file, indent=4)

add_persons_to_json(2)
