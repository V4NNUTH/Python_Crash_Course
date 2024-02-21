sandwich_order =  [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']

finished_sandwich = []
print("\n")
print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

print("\n")
while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwich.append(current_sandwich)

print("\n")
print(finished_sandwich)
print("\n")
for sandwich in finished_sandwich:
    print("I made a " + sandwich + " sandwich.")
