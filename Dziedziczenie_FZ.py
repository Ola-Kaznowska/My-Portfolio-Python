class Flipper():
    def __init__(self,kolor="Biały", level=1):
        self.kolor = kolor
        self.level = level
        

class Hacking(Flipper):
    def __init__(self, kolor, level):
        super().__init__(kolor,level)
        
        

Delfinek = Flipper("Biały", 1)
Aplikacja = Hacking("QFlipper", 3)

print(Delfinek.level)
print(Delfinek.kolor)
print(Aplikacja)


print(type(Delfinek))
print(type(Aplikacja))



print("Jakiego koloru jest Flipper Zero?", str(isinstance(Delfinek, Flipper)))
print("Jaka nazywa się aplikacja do obsługi Flipper'a Zero i ile ich jest", str(isinstance(Aplikacja, Hacking )))