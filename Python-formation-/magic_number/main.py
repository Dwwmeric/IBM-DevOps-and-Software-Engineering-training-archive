import random

nb_min = 1
nb_max = 10
nb_magic = random.randint(nb_min, nb_max)
result = 0
life_max = 3

def request_nbr(nb_min , nb_max):
    nb_int = 0
    while nb_int == 0: 
        
        nb_choise = input(f"What is the magic number between {nb_min} and {nb_max} ?")

        try:
            nb_int = int(nb_choise)
        except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        else:
            if nb_int < nb_min or nb_int > nb_max: 
                print(f"Oops! The number is not comprehended between {nb_min} and {nb_max}.  Try again...")
                nb_int = 0
        
    return nb_int 


while result != nb_magic and life_max != 0:

        print(f"Your life is {life_max} !!!")
        result = request_nbr(nb_min , nb_max , life_max) 
        
        if result > nb_magic:
            print("The magic number is smaller!")
            life_max -= 1
        elif result < nb_magic:
            print("The magic number is greater!")
            life_max -= 1
        else:
            print("Brave you have found the magic number!!!")
            break

if life_max == 0:
    print("Game Over !!!")
