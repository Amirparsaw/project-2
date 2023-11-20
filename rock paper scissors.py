import random

match_count = int(input("how much do you play => "))
inp_points = 0
comp_points = 0

while inp_points < 3 and comp_points < 3:
    inp_data = input("Enter your choice(rock or paper or scissor ) => ")
    comp_data = random.choice(["rock", "paper", "scissor"])
    print(f"your choice is {inp_data} and your rival choice is {comp_data}")

    if inp_data == "rock" and comp_data != "rock":
        inp_points += 1
    elif comp_data == "rock" and inp_data != "rock":
        comp_points +=1

    elif inp_data == "paper" and comp_data == "rock":
        inp_points += 1

    elif comp_data == "paper" and inp_data == "rock":
        comp_points += 1

    elif inp_data == "rock" and comp_data == "scissor":
        inp_points +=1

    elif comp_data == "rock" and inp_data == "scissor":
        comp_points +=1

    elif inp_data == "scissor" and comp_data == "paper":
        inp_points +=1

    elif comp_data == "scissor" and inp_data == "paper":
        comp_points +=1

    elif inp_data == comp_data:
        print("It's a tie!")
        continue
        
    print(f"inp_points:{inp_points} and comp_pints:{comp_points}")

if inp_points > comp_points:
    print(f"You won the game : your score is {inp_points}")
else:
    print(f"The computer won the game : your score is {comp_points}")
