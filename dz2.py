def ask_password():
    password = "password"  
    attempts = 3 
    for i in range(attempts):
        user_input = input()  
        if user_input == password:
            print("Пароль принят")
            return
    print("В доступе отказано")

ask_password()