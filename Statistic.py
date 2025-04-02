import numpy as np

list1 = [6, 8, 2, 4, 5, 9]
list2 = [6, 8, 2, 4, 5, 9 ,3]

def calculate_median(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        return (lista[len(lista)//2 ]+ lista[len(lista)//2]) /2
    else:
        return lista[len(lista)//2]
    
print(f"Median list1: {calculate_median(list1)}")
print(f"Median list2 {calculate_median(list2)}")