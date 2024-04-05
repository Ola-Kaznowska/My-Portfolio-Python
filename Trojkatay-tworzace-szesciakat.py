import turtle

turtle.pensize(5)



def draw_a_triangle(n): #Tworzę funkcję przymującą jeden argument n
    for i in range(3):
        turtle.forward(n) #Odwołuję się do funkcji aby narysować trójkąt o podanej długośći jako argument
        turtle.left(120)
        
        
for i in range(6):
    draw_a_triangle(300) #Odwołuję się do funkcji
    turtle.left(60)