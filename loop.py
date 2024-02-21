unconfirm_user = ['sok','sao','nuth']

confirm_user = []

while unconfirm_user:
    current_user = unconfirm_user.pop()

    print(f"Verifying user: {current_user.title()}")
    confirm_user.append(current_user)
print("\n\n\n")
print(confirm_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirm_user:
    print(confirmed_user.title())