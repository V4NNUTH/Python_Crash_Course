from random import randint


class Dic():
    
    def __init__(self, side = 6):
        self.side = side

    def roll_die(self):
        return randint(1,self.side)

d6 = Dic()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print("\n10 roll of a 6-side die:")
print(results)

d20= Dic(side = 20)
results = []
for rull_num in range(10):
    result = d20.roll_die()
    results.append(result)

print("\n10 roll of a 20-side die:")
print(results)




