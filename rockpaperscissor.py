"""
WORKFLOW OF THE PROGRAM:
1. USER CHOICE: INPUT FROM USER (Rock, Paper, Scissor)
2. COMPUTER CHOICE: COMPUER CHOOSES RANDOMLY (Rock, Paper, Scissor)
3. PRINT THE RESULT

Cases:
A: Rock:-
    Rock - Rock = Tie
    Rock - Paper = Paper win
    Rock - Scissor = Rock win

B: Paper:-
    Paper - Paper = Tie
    Paper - Rock = Paper win
    Paper - Scissor = Scissor win

C: Scissor:-
    Scissor - Scissor = Tie
    Scissor - Rocl = Rock win
    Scissor - Paper = Scissor win

"""
import random
choices = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move (Rock, Paper or Scissor):  ")
comp_choice =  random.choice(choices)
if user_choice != "Rock" and user_choice != "Paper" and user_choice != "Scissor":
    print("The choice is invald... Please choose among : Rock, Paper and Scissor")
print(f"User choice = {user_choice}\nComputer choice = {comp_choice}")
if user_choice == comp_choice:
    print("Choices are same: Match tied")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers rock: Computer wins")
    else:
        print("Rock smashes scissor: You win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper covers rock: You win")
    else:
        print("Scissor cuts paper: Computer wins")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes scissor: Computer wins")
    else:
        print("Scissor cuts paper: You win")

