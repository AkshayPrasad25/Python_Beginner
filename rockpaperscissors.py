import random
sd=''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ganme_images=[sd,rock,paper,scissors]
yourchoice=int(input("Choose Rock Paper or Scissors: (1-Rock,2-paper,3-Scissors):\n"))
print(ganme_images[yourchoice])
computer_choice=random.randint(1,3)
print(f'Computer chose')
print(ganme_images[computer_choice])
if computer_choice==yourchoice:
    print("DRAW! NO ONE WINS")
elif yourchoice>=4 or yourchoice<1:
    print("Invalid number input")
elif yourchoice==1 and computer_choice==3:
    print("YOU WIN!!YAY")
elif computer_choice==1 and yourchoice==3:
    print("YOU LOSE!!")
elif computer_choice>yourchoice:
    print("YOU LOSE")
elif yourchoice>computer_choice:
    print("YOU WIN!! YAY")
