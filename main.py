def game():
 import random
 # 1 for rock
 # 0 for scissor
 # -1 for paper

 # Computer randomly selects between rock, scissor, or paper

 comp=random.choice([1,0,-1])
 # Get user's choice
 youstr=input("enter input:")

 # Mapping user input to game choices
 revDict={"r":1,"s":0,"p":-1}
 youDict={1:"rock", 0:"scissor",-1:"paper"}

 # Convert user's input to the corresponding game choice
 you = revDict[youstr]

 # Display choices made by the user and the computer
 print(f"You chose {youDict[you]}\nComputer chose {youDict[comp]}")

 # Determine the result of the game



 if(comp==you):
  # If both choices are the same, it's a draw
         print("It's a Draw")
 else:

    # Determine win/lose based on game rules

    if(comp==1 and you==0): #rock hits scissor
     print("You Lose!")
    elif(comp==1 and you==-1): #paper covers rock
        print("You Win!")
    elif(comp==0 and you==1): #rock hits scissor
        print("You Win!")
    elif(comp==0 and you==-1): #scissor cuts paper
        print("You Lose!")
    elif(comp==-1 and you==1): #paper covers rock
        print("You Lose!")
    elif(comp==-1 and you==0): #scissor cuts paper
        print("You Win!")
    else:
        print("Something went wrong! Please try again")

#Asking user whether he want to play the game or not
 again=input("Do you want to play agian?\n('y' for Yes/'n' for No)")

 if(again=="y"):
    game()
 else:
    print("Thank you playing!")
    
#start game
game()