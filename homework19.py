# დააგენერირეთ სტუდენტის დიქშენერების 100 ელემენტიანი სია
# სახელების, გვარების და იმეილების რენდომულად დასაგენერირებლად
# გამოიყენეთ faker მოდული

# სტუდენტს უნდა ჰქონდეს შემდეგი key-ები და შესაბამისი value-ები:
# first_name - გამოიყენეთ faker
# last_name - გამოიყენეთ faker
# email - გამოიყენეთ faker
# age - 18დან 70 წლამდე(შემთხვევითი პრინციპით)
# is_active - (True ან False) რანდომულად

# არსებული სია json მოდულის დახმარებით ჩაწერეთ ფაილში

# შემდეგ წაიკითხეთ ეს ფაილი json მოდულის დახმარებით, 
# გაფილტრეთ სტუდენტები is_active ქის მიხედვით, ისეთი სტუდენტები რომლის is_active
# არის True, შეიტანეთ ლისტში და ჩაწერეთ ახალ ფაილში


import json
import random
from faker import Faker

fake = Faker()

students = []
for _ in range(100):
    student = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }
    students.append(student)

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4, ensure_ascii=False)

with open("students.json", "r", encoding="utf-8") as file:
    students_data = json.load(file)

active_students = [student for student in students_data if student["is_active"]]

with open("active_students.json", "w", encoding="utf-8") as file:
    json.dump(active_students, file, indent=4, ensure_ascii=False)


print("Generated students:", students[:3]) 
print("Active students:", active_students[:2])  