def who_are_you_and_hello():
    while True:
        name = input()
        if name.isalpha() and name == name.capitalize() and name[1:].islower():
            print(f"Привет, {name}!")
            break