import math 

basketballTrainingFee = int(input("State how much money you have: "))
basketballSneekers = basketballTrainingFee * 0.6
basketbaalOutfit = basketballSneekers * 0.8
ball = basketbaalOutfit * 0.25
basketballAccesories = ball * 0.2

print(basketbaalOutfit)   
print(basketballSneekers)
print(ball)
print(basketballAccesories)  


finalSum = basketballTrainingFee + basketballSneekers + basketbaalOutfit + ball + basketballAccesories
print(finalSum)