passwords = [
    # {"service": "acebook", "password": "password123", "added_on": "22/03/22"},
    {"service": "makersbnb", "password": "qwerty789", "added_on": "22/03/22"},
    {"service": "acebook", "password": "qwsdfdsfsdfsdfsd", "added_on": "22/03/22"},
]

# using the filter method
def is_acebook(password):
    return password["service"] == "acebook"

print(next(filter(is_acebook, passwords)))

# using a lambda (anonymous function) instead of the is_acebook function
print(next(filter(lambda password: password['service'] == 'acebook', passwords)))