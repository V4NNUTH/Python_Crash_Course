
from random import choice

def win_tickets(num):
    win_ticket=[]
    while len(win_ticket) < 4:
        pull = choice(num)
        if pull not in win_ticket:
            win_ticket.append(pull)
    return win_ticket

def your_ticket(num):
    my_ticket = []
    while len(my_ticket)< 4:
        pull= choice(num)
        if pull not in my_ticket:
            my_ticket.append(pull)
    return my_ticket

def check_ticket(play_ticket, win_ticket):
    if play_ticket == win_ticket:
        for element in play_ticket:
            if element not in win_ticket:
                return False
        return True
    return False



num = [1,2,3,4,5,6,7,8,9,'a','b','c','d','e']
win = win_tickets(num)
play = 0
max_random = 1000000
hi = False

while not hi:
    my = your_ticket(num)
    hi = check_ticket(my,win)
    play +=1
    if play >= max_random:
        break


if  hi:
    print("====Here your Ticket====")
    print(f"Your Ticket:{my}")
    print(f"winning Ticket:{win}")
    print(f"It's pull over {play} times for your Ticket win!")

else:
    print(f"Tries {play} times, without pulling a winning.")
    print(f"Your Ticket: {my}")
    print(f"Winning ticket: {win} .")
