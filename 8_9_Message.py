
def show_message(*text):
    for n_text in text:
        print(f"Message:{n_text}")

    return n_text

new_text=['Hi','Hello','Bonjour','Good Bye']
hi=['car','moto']
show_message(new_text)
show_message(hi)
print("\n")
print(new_text)
def send_message(n_text, sends_messages):
    while n_text:
        current_message = n_text.pop()
        print(current_message)
        sends_messages.append(current_message)
    for new_messages in sends_messages:
        print(f"The Message:{new_messages}")
    
sends_messages=[]
send_message( new_text[:] ,sends_messages)
print("\n")

print(new_text)
print(sends_messages)