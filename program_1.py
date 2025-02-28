#By: Sabria Fafach
#Date: Febuary 28, 2025
#Name: program_1.py


import random
NUMBER_OF_DICE_ROLLS=100

def randDice():
    number_1=random.randint(1,6)
    number_2=random.randint(1,6)
    tot_roll=number_1+number_2
    return tot_roll

#########

def main():
    total=0
    for num in range(NUMBER_OF_DICE_ROLLS):
        roll=randDice()
        total=total+roll
    average=total/NUMBER_OF_DICE_ROLLS
    print(f"The average roll of one hundred dice rolls is: {average:.2f}")

main()
