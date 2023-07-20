passwords = [
    {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
    {"service": "makersbnb", "password": "qwerty789", "added_on": "22/03/22"},
    {"service": "acebook", "password": "qwsdfdsfsdfsdfsd", "added_on": "22/03/22"},
]

# using the filter method
def is_acebook(password):
    return password["service"] == "acebook"

print(next(filter(is_acebook, passwords)))

# using a lambda (anonymous function) instead of the is_acebook function
print(next(filter(lambda password: password['service'] == 'acebook', passwords)))

# practice v1
def are_all_passwords_long_enough(passwords):
    for password in passwords:
        if len(password['password']) < 8:
            return False
    return True

print(are_all_passwords_long_enough(passwords))
# => false

# practice v2
