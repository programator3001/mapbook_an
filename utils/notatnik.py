users: list = [
    {"name": "Bernard", "location": "Ełk", "posts": 400},

]
print(users)

def remove_user(users_data: list)->None:

    user_name=input("podaj imię użytkownika do usunięcia: ")
    for user in users_data:
        if user["name"] == user_name:
             users_data.remove(user)

remove_user(users)
