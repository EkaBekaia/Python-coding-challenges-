# 1. დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს რიცხვს, რა რიცხვსაც გადავცემთ, იმდენჯერ შეეკითხება მომხმარებელს 
#    სახელს, გვარს და ასაკს. ანუ თუ გადავეცით 3, 3-ჯერ შეეკითხება მომხმარებელს აღნიშნულ ინფორმაციას, ინფუთის 
#    საფუძველზე csv ფაილში ჩაწერეთ შესაბამისი ინფორმაცია შემდეგი სახით, მაგალითად:

#    ID,first_name,last_name,age
#    1,John,Doe,25
#    2,Alice,White,30

#    და ა.შ.
   
# #    გამოიყენეთ try, ecxept იმისათვის რომ მომხმარებელმა ასაკის შემოყვანის დროს აუცილებლად ინტეჯერი შემოიყვანოს!
# #    ფაილში ჩასაწერად აუცილებლად გამოიყენეთ csv მოდულიდან writer და DictWriter!

import csv

def user_info(trial):
 
    filename = 'user_data.csv'
    
 
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
      
        writer.writerow(['ID', 'first_name', 'last_name', 'age'])
        
        for i in range(1, trial + 1):
            print(f"Please enter the information for user {i}:")
            
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            
           
            while True:
                try:
                    age = int(input("Age: "))
                    break
                except ValueError:
                    print("Please enter a valid age (number).")
            
          
            writer.writerow([i, first_name, last_name, age])

user_info(2)

     
# 2. მიმაგრებულ students.csv ფაილიდან წაიკითხეთ ინფორმაცია, გაფილტრეთ Grade-ის მიხედვით შემდეგნაირად:
#    ყველა სტუდენტი, რომელსაც 50-ზე ნაკლები ქულა აქვს შეინახეთ ახალ ფაილში(failed_students.csv)
#    ყველა სტუდენტი, რომელსაც 50-ზე მეტი ქულა აქვს შეინახეთ ახალ ფაილში(passed_students.csv)

#    ფაილებიდან ინფორმაციის წასაკითხად და ჩასაწერად აუცილებლად გამოიყენეთ DictReader და DictWriter!

import csv


source_file = 'students.csv'


failed_filename = 'failed_students.csv'
passed_filename = 'passed_students.csv'


with open(source_file, mode='r', newline='') as input_file:
    reader = csv.DictReader(input_file)

   
    students_data = {'failed': [], 'passed': []}

   
    for row in reader:
       
        try:
            grade = float(row['Grade'])
            if grade < 50:
                students_data['failed'].append(row)
            else:
                students_data['passed'].append(row)
        except ValueError:
            print(f"Skipping invalid data in row: {row}")


with open(failed_filename, mode='w', newline='') as failed_file:
    fieldnames = ['ID', 'First Name', 'Last Name', 'Grade'] 
    writer = csv.DictWriter(failed_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students_data['failed'])


with open(passed_filename, mode='w', newline='') as passed_file:
    writer = csv.DictWriter(passed_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students_data['passed'])




class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, number, age, nationality):
        player = {
            "name": name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality
        }
        self.players.append(player)
        print(f"Player {name} added successfully!")

    def delete_player(self, number):
        for player in self.players:
            if player["number"] == number:
                self.players.remove(player)
                print(f"Player {player['name']} removed successfully!")
                return
        print("Player not found!")

    def update_information(self, number, key, value):
        for player in self.players:
            if player["number"] == number:
                player[key] = value
                print(f"Updated {key} for player {player['name']} to {value}")
                return
        print("Player not found!")

    def club_info(self):
        print(f"Club Name: {self.team_name}")
        print(f"Coach: {self.coach}")
        print("Players:")
        for player in self.players:
            print(f"  {player['name']} - {player['position']} - #{player['number']}")

    def player_info(self, number):
        for player in self.players:
            if player["number"] == number:
                print("Player Information:")
                for key, value in player.items():
                    print(f"  {key.capitalize()}: {value}")
                return
        print("Player not found!")

