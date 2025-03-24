# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება მართკუთხა სამკუთხედის კათეტების სიგრძეს(მთელი დადებითი რიცხვი)
#  და გამოითვლის  ამ სამკუთხედის ჰიპოთენუზის სიგრძეს და ფართობს.

#Understand the problem
#1.How to calculate  length of the hypotenuse? Answer: add the squared values of legs and Take the square root from 
#2.How to calculate  the are of right triangle? Area = (1/2) × base × height

#Breaking into sub-tasks
#1. Ask user to define leg 1 and leg2
#2. Calculate hypotenuse and area
#3. Print hypotenuse and area


leg1=int(input('Input length of 1st leg: '))
leg2=int(input('Input length of 2nd leg: '))

hypotenuse=(leg1 ** 2 + leg2 ** 2) ** 0.5
area = (leg1 * leg2) / 2

print(f"Hypotenuse is: {hypotenuse} and Area is {area}")


# ----------------------------------------------------------------------------------------
# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება წამების რაოდენობას და გამოიტანეთ საათების, წუთების და წამების
# რაოდენობას (მაგ. 20000 წამი არის  5 საათი, 33 წუთი, 20 წამი)

seconds=int(input('Input desiredn number of seconds:'))

hours=seconds//3600
minutes=seconds%3600//60
seconds=seconds%3600%60

print (f"{hours} hours, {minutes} minutes, {seconds} seconds")



