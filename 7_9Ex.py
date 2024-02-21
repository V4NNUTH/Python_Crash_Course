name_prompt = "\nWhat's your name:  "
place_prompt = "If you could visit one place in the world, where would it be:  "
continue_prompt = "\nWould you like to let someone else respond(yes/no):   "

responese = {}

name = input(name_prompt)
place = input(place_prompt)


while True :
    responese[name]=place
    
    continues = input(continue_prompt)

    if continues != 'yes':
        break

print("\n-----Result-----")
for name , place in responese.items():
    print(name.title()+" the place would to go is "+ place.title()+".")

