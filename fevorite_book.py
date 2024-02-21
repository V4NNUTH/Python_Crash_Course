def fev_book(book):
    name = input("What is your name: ")
    print(f"Hello {name.title()} your fevorite book is {book.title()}")

fev_book("python")

print("\n\n")

def describe_city(city , country ="cambodia"):

    print(f"{city.title()} is in {country.title()}")

describe_city("Takeo")
describe_city("badombong")
describe_city("phnom penh")