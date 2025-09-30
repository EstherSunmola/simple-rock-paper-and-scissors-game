import random


rock='''
    
       _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
paper= '''
   
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''
scissors='''
     
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
     '''
    
game=[rock,paper,scissors]
choice=input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')

choice_in=random.choice(game)


     
rock=0
paper=1

    
    
if choice==choice_in:
    print("its a draw")
elif choice==0 and choice_in==2:
    print("you win!")
elif choice==1 and choice_in==0:
    print("you win!")
elif choice==2 and choice_in==1:
    print("you win!")  
elif choice_in==0 and choice==2:
    print("you lose!")
elif choice_in==1 and choice==0:
    print("you lose!")
elif choice_in==2 and choice==1:
    print("you lose!")          
           
    
  