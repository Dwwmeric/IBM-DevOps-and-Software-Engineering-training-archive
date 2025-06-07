import random

nb_min = 1
nb_max = 10
nb_question = 4
nb_point = 0 

def question_generate():

    nb_1 = random.randint(nb_min, nb_max)
    nb_2 = random.randint(nb_min, nb_max)
    operateur = [" - ", " + ", " * " , " / "]
    random_operateur = random.choice(operateur)

    result = int(input(f"Calculate: {nb_1}{random_operateur}{nb_2} = "))
    calcul = str(nb_1) + random_operateur + str(nb_2)
    if result == eval(calcul):
        print(f"Correct , the result is indeed {result} !\n")
        point = 1 
    else:
        print(f"Incorrect, {result} is not the resulta! The correct answer is {eval(calcul)}.\n")
        point = 0
    
    return point

for i in range(0,nb_question):
    print(f"Quention {i + 1} of {nb_question}")
    point = question_generate()
    nb_point += point

print(f"Your result is {nb_point} / {nb_question}")

if nb_point == nb_question:
    print("Good job !!!")
elif nb_point == 0:
    print("You have to go revise your math...")
elif nb_point > int(nb_question / 2): 
    print("well done")
else :
    print("little better")
