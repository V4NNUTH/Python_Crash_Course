import json
filename = 'username.json'
try:
    with open(filename)as f:
        user_name = json.load(f)
except FileNotFoundError:
    user_name = input("What is your name: ")
    with open(filename, 'w') as f:
        json.dump(user_name,f)
        print("We will remember you when you come back,{}".format(user_name))
else:
    print("welcome back, {}!".format(user_name))