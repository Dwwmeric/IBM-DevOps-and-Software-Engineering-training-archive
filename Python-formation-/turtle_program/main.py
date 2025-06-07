import turtle

t = turtle.Turtle()

# exercice one 
# int = 5

# for i in range(int):
#     t.forward(30)
#     t.left(90)
#     t.forward(30)
#     t.right(90)



# def esclalator(taille , nb ):
#     for i in range(nb):
#         t.forward(taille)
#         t.left(90)
#         t.forward(taille)
#         t.right(90)
#     t.forward(taille)

# esclalator( 45 , 7)

int = 4
def square (side):
    for i in range(int):
        t.forward(side)
        t.left(90)

def squares(side , nb):
    # square(side)
    for i in range(nb):
        square((i + 1) * side)

squares(22 , 4)

turtle.done()