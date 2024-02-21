users = {
    'vannuth':{
        'first':'ven',
        'last':'vannuth',
        'location':'takeo',
    },
    'aeinstein':{
        'first':'albert',
        'last':'aeinstein',
        'location':'paris',
    },
}

for user_name , user_info in users.items():
    print(f"\nUsername: {user_name}")
    fullname = f"{user_info['first']} {user_info['last']}"
    locations = user_info['location']

    print(f"\tFull Name: {fullname.title()}")
    print(f"\tLocation: {locations.title()}")

