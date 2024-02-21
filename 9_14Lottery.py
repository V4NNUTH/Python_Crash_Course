from random import choice

pos = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
def win(pos):
    winning_ticket = []
    print("Let's see what the winning ticket is ....")
    while len(winning_ticket)<4:
        pulled_item = choice(pos)
        if pulled_item not in winning_ticket:
            print(f"We pulled  a {pulled_item}!")
            winning_ticket.append(pulled_item)
    return winning_ticket       

res =win(pos)
print(f"The final winning is :{res}")