# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს უსასრულოდ შეეკითხება ჯერ სახელს, შემდეგ გვარს და რაიმე ფაილში ჩაწერს 
#    სახელს და გვარს ერთ ხაზზე თავისი ნუმერაციით, ყველა ახალი სახელი და გვარი უნდა იყოს ახალ ხაზზე ჩაწერილი, მაგალითად:
   
#    Enter your first name: Otar
#    Enter your last name: Tumanishvili
#    Enter your first name: Nika
#    Enter your last name: Papaskiri
#    Enter your first name: stop

#    ფაილში უნდა ჩაიწეროს შემდეგი სახით:
#    1. Otar Tumanishvili
#    2. Nika Papaskiri


#    პროგრამა ჩერდება იმ შემთხევაში, თუ მომხმარებელმა სახელის ადგილას შეიყვანა სიტყვა stop


file = open("name.txt", "a")
count = 1

while True:
    first_name = input("Enter your first name: ")
    if first_name.lower() == "stop":
        break
    last_name = input("Enter your last name: ")
    file.write(f"{count}. {first_name} {last_name}\n")
    count += 1

file.close() 

file = open("name.txt", "r") 
print(file.read())  
file.close() 



# 2. თანდართულ ფაილში "persons.txt" მოცემულია ადამიანების სია შემდეგი ფორმატით:
#    სახელი და გვარი, ასაკი, ქალაქი

#    Evelyn Cook, 75, Nixonland
#    Dr. Briana Davidson, 22, South Hunterside
#    ...
#    ...

#    თქვენი დავალებაა არსებული ფაილიდან წაიკითხოთ ინფორმაცია, შექმნათ ორი ახალი ტექსტური ფაილი (.txt გაფართოებით), ერთ ფაილში
#    ჩაწერეთ ყველა პიროვნება რომლის ასაკი ნაკლებია 50-ზე, ხოლო მეორე ფაილში ჩაწერეთ ყველა პიროვნება, რომლის ასაკი მეტია 50-ზე,
#    ფორმატი დაცული უნდა იყოს ისეთი სახით, როგორიც არის ორიგინალ "persons.txt" ფაილში ანუ თითო პიროვნება თითო ხაზზე!

with open("persons.txt", "r") as file:
    lines = file.readlines()

under_50 = []
over_50 = []


for line in lines:
 
    name, age, city = line.strip().split(", ")
    age = int(age)  
   
    if age < 50:
        under_50.append(line.strip())
    else:
        over_50.append(line.strip())


with open("under_50.txt", "w") as file:
    for person in under_50:
        file.write(person + "\n")


with open("over_50.txt", "w") as file:
    for person in over_50:
        file.write(person + "\n")

