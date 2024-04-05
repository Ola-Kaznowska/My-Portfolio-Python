import turtle 

turtle.pensize(3)
turtle.pencolor("#ff0000") #Kolor osiemnastokątu w zapsie HEX'a czerwony

for i in range(18): #Tworzę pętlę for która ma sie powtórzyć 18 rzy ponieważ potrzebuję 18 kątów
    turtle.forward(40)
    turtle.left(20)