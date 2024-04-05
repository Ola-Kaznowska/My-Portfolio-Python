import turtle #Importuje moduł Turtle

turtle.pensize(10) #Grubość rysowanej linii

for i in range(8): #Powtarzam pętlę for 8 razy ponieważ potrzebuję 8 razy powtórzyć kąt
    turtle.forward(100) #Idę prosto przez 100 pikseli
    turtle.left(45) #Kąt 45 stopni