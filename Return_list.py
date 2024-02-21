def name(user_name):
    for user_name in user_name:
        your_name = f"\nHello! {user_name.title()}"
        print(your_name)
        
def name2(na):
    n_name = f"Your name {na.title()}"
    print(n_name)
my_name = ["vannuth",'sok','sao']
you_name = {"Name":"Ven Vannuth",
            "Location":"Takeo"}
name(my_name)
name2(you_name["Name"])