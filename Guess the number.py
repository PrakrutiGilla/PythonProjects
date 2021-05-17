import random

def user_guess(x):

   num=random.randint(1,x)
   guess=0
   lives=5
   while(num!=guess and lives>0):
            guess=int(input("Enter a number"))
            lives=lives-1
    
            if(num>guess):
                print("Your number is low")
            else:
                print("Your number is high")

            print("You have only ",lives," more chances")

   if(num==guess):      
            print(f"Your guess is right, the number is {num}")

   else:
            print("Better luck next time! The number is",num)


def computer_guess(x):
    low=0
    high=x
    feedback=" "
    
    while(feedback!="c"):
        guess=random.randint(low,high)
        feedback=input(f"Is {guess} High(H)or Low(L) or Correct(C)").lower()
        
        if(feedback=="h"):
            high=guess-1

        else:
            low=guess+1
            

    print(f"The guess is right, the number is {guess}")        

computer_guess(100)             
            
            
