import random

def score_board(a,b):

  print("Your score      : ",a)
  print("Opponent's score: ",b)
  
  if(a>b):
    print("You Won!")

  elif(a<b):
    print("You Lost!")

  else:
    print("It's a tie")



i=int(input("No of times you wanna play"))
user_count=0
computer_count=0

while(i>0):
  user=input("What's your choice? 'p' for paper, 'r' for rock, 's' for scissors").lower()
  computer=random.choice(['r','p','s'])
  print("Opponent got ",computer)
  i=i-1
  
  if((user=='r' and computer=='s')or(user=='p' and computer=='r')or(user=='s' and computer=='p')):
    user_count=user_count+1  
    print("You Win")

  elif(computer==user):
    print("It is a tie")
    
  else:
    computer_count=computer_count+1  
    print("You Lost")
    

print("Match is over")
score_board(user_count,computer_count)

