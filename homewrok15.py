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


# წინა დავალება გადააკეთეთ შემდეგნაირად:

# ცალკე შექმენით მოთამაშის კლასი შემდეგი ატრიბუტებით:
# მოთამაშის აიდი: ავტომატურად ენიჭებოდეს და იზრდებოდეს ერთით ყოველი მოთამაშის ობიექტის შექმნისას,
# სახელი, პოზიცია, სათამაშო ნომერი(private), ასაკი(private) და ეროვნება.

# მეთოდები:
# მოთამაშის სრული ინფორმაციის ჩვენება,
# __str__,
# სურვილისამებრ შეგიძლიათ დაუმატოთ მეთოდები

# ცალკე შექმენით მწვრთნელის კლასი შემდეგი ატრიბუტებით:
# სახელი და გამოცდილების წლები(private).

# მეთოდები:
# მწვრთნელის სრული ინფორმაციის ჩვენება,
# __str__
# სურვილისამებრ შეგიძლიათ დაუმატოთ მეთოდები

# საბოლოოდ შექმენით Team კლასი შემდეგი ატრიბუტებით:
# სახელი, მწვრთნელი(მწვრთნელის ობიექტი) და მოთამაშეები(მოთამაშის ობიექტების სია).
# მეთოდები:
# მოთამაშის დამატება,
# მოთამაშის ძებნა აიდის მიხედვით და ინფორმაციის გამოტანა,
# მოთამაშის ინფორმაციის განახლება(წინა დავალების ანალოგიურად ოღონდ აიდის მიხედვით),
# მოთამაშის წაშლა(აიდის მიხედვით),
# კლუბის სრული ინფორმაციის ჩვენება(სახელი, მწვრთნელი, მოთამაშეები),
# __str__

# ბონუსი: კლუბში ვერ უნდა ემატებოდეს 25 მოთამაშეზე მეტი,
# აწარმოეთ მოთამაშის სტატისტიკა(რამდენი მატჩი ითამაშა, რამდენი გოლი გაიტანა და ა.შ.)


class Player:
    id_counter = 1
    
    def __init__(self, name, position, number, age, nationality):
        self.id = Player.id_counter
        Player.id_counter += 1
        self.name = name
        self.position = position
        self.__number = number
        self.__age = age
        self.nationality = nationality
        self.stats = {"matches": 0, "goals": 0}

    def show_info(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Number: {self.__number}, Age: {self.__age}, Nationality: {self.nationality}, Stats: {self.stats}"
    
    def __str__(self):
        return self.show_info()

class Coach:
    def __init__(self, name, experience_years):
        self.name = name
        self.__experience_years = experience_years
    
    def show_info(self):
        return f"Coach Name: {self.name}, Experience: {self.__experience_years} years"
    
    def __str__(self):
        return self.show_info()

class Team:
    def __init__(self, name, coach):
        self.name = name
        self.coach = coach
        self.players = []
    
    def add_player(self, player):
        if len(self.players) < 25:
            self.players.append(player)
            print(f"Player {player.name} added successfully!")
        else:
            print("Cannot add more players, team is full!")
    
    def find_player(self, player_id):
        for player in self.players:
            if player.id == player_id:
                return player
        return None
    
    def update_player_info(self, player_id, key, value):
        player = self.find_player(player_id)
        if player:
            player.stats[key] = value
            print(f"Updated {key} for player {player.name} to {value}")
        else:
            print("Player not found!")
    
    def remove_player(self, player_id):
        player = self.find_player(player_id)
        if player:
            self.players.remove(player)
            print(f"Player {player.name} removed successfully!")
        else:
            print("Player not found!")
    
    def show_team_info(self):
        print(f"Team: {self.name}, Coach: {self.coach.name}")
        for player in self.players:
            print(player)
    
    def __str__(self):
        return f"Team: {self.name}, Coach: {self.coach.name}, Players: {[player.name for player in self.players]}"


team = Team("PSG", Coach("Luis Enrique", 10))
team.add_player(Player("Khvicha Kvaratskhelia", "Forward", 7, 23, "Georgia"))
team.add_player(Player("Georges Mikautadze", "Striker", 9, 23, "Georgia"))
team.show_team_info()
team.update_player_info(1, "goals", 5)
team.show_team_info()
team.remove_player(2)
team.show_team_info()