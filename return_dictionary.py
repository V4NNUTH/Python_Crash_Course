from ast import While


def name(first,last,age):
    person = {'first_name':first,'last_name':last}
    if age:
        person['age'] = age

    return person

the_name =name("ven","vannuth","27")
print(the_name)

def buy_car(your_name, car):
    print("---Here is your information---")
    info = f"Hello {your_name} your car that you order is {car}"
    return info
while True:
    print("---Please Enter some Information---")
    print("Enter no if your don't want enter anymore!")
    your_name = input("Enter your name:")
    if(your_name)=='no':
        break
    car= input("Enter car what you want: ")
    if (car)=='no':
        break
    print("\n\n")
your_info = buy_car(your_name,car)
print("\n")
print(your_info)
