import numpy as np 


arr = np.array([ [1,2,3], ["Python", "is", "cool"], [4,5,6]])

print(arr)

print(arr.ndim)

print()



print(f"My elments is: {arr[1, 0]}")


print()




table = arr[1:2]

print(table)


print()




Tab = np.array(["Hi", "My", "Name", "is", "Ola", "I'm", "Python", "Developer"])

Two_Tab = Tab.copy()
Two_Tab[4] = "JustJoinIT"


print(Tab[::3])

print()

print(Tab)
print(Two_Tab)



print()

print(np.__version__)