dic = {
    "username": "mri",
    "pass": "12345678",
    "name": "maream saad",
    "age": 21,
    "mail": "mri@mail.ru",
}

attempts3 = 3
attempts = 0

while attempts < attempts3:
    User = input("Enter Your Username: ")
    Pass = input("Enter Your Password: ")

    if User == dic["username"] and Pass == dic["pass"]:
        print(f"Welcome {dic['name']}\nYour Age is {dic['age']}\nYour Mail is {dic['mail']}")
        break
    else:
        attempts += 1
        remaining = attempts3 - attempts
        
        if remaining > 0:
            print(f"Username or Password Wrong — {remaining} attempt left\n")
        else:
            dic.clear()
            print("Account locked"
