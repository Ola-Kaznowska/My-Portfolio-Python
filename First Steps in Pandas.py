import pandas as pd 

data = {"Aleksandra": 30, "Antoni": 31, "Jan": 32, "Bartosz": 33, "Karol": 34}
s = pd.Series(data)
print(s)

print()

s = pd.Series([1, 2, 3, 4, 5, pd.NA], index = ["a", "b", "c", "d", "e", "nieznane"])
print(s)

print()

data = {
    "cena" : [15, 30, 25],
    "ilosc" : [30, 40, 20]
}

df = pd.DataFrame(data, index = ["dzien 1", "dzien 2", "dzien 3"])
print(df)

print()

print(df.info())