

def name_car(car , new_car):
    while car:
        current_car = car.pop()
        new_car.append(current_car)

def show_car(new_cars):
    print("---Hear is your car---")
    for new_cars in new_car:
        print(f"\nYour model car is {new_cars}")
        
car = ["BMW","Toyota","Tesla","Lembogini","ferrari"]
new_car = []

name_car(car, new_car)
show_car(new_car)