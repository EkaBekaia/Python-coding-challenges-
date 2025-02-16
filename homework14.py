# Football Team Managmenet System

# შექმენით კლასი FootballTeam შემდეგი ატრიბუტებით:
# team_name (string) - კლუბის სახელი
# coach (string) - მწვრთნელი
# players - მოთამაშეების სია(შექმნისას ცარიელი უნდა იყოს)

# კლასს უნდა გააჩნდეს შემდეგი მეთოდები:
# 1. მოთამაშის დამატება - მოთამაშის სახელი, პოზიცია, სათამაშო ნომერი, 
#    ასაკი და ეროვნება(დიქტის სახით უნდა დაემატოს მოთამაშეების სიაში)

# 2. მოთამაშის წაშლა - მოთამაშე უნდა წაიშალოს სიიდან სათამაშო ნომრის მიხედვით

# 3. მოთამაშის ინფორმაციის განახლება - მოთამაშე უნდა მონახოთ სათამაშო ნომრის მიხედვით
#    და უნდა დაუსეტოთ ისეთი ინფორმაცია, რომელსაც გადასცემთ ამ მეთოდს, მაგ: "goal": 1 
#    ანუ key და value უნდა იყოს გადაცემული ამავე მეთოდის გამოძახებისას!

# 4. კლუბის ინფორმაციის ჩვენება - გამოიტანეთ კლუბის სახელი, მწვრთნელის სახელი და მოთამაშეების სია

# 5. მოთამაშის ინფორმაციის ჩვენება - უნდა გამოიტანოთ ინფორმაცია მოთამაშის ნომრის მიხედვით

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

# Example Usage
team = FootballTeam("Barcelona", "Name Surname")
team.add_player("Lionel Messi", "Forward", 3, 36, "Argentina")
team.add_player("Cristiano Ronaldo", "Forward", 5, 39, "Portugal")
team.club_info()
team.player_info(3)
team.update_information(3, "goals", 5)
team.player_info(3)
team.delete_player(5)
team.club_info()
