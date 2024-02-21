def built(first, last, **user_info):
    user_info['first_name']= first
    user_info['last_name']= last

    return user_info

user = built('Ven','Vannuth',locatin='Takeo',filed='Data Science',newLocation="Phnom Penh")
print(user)