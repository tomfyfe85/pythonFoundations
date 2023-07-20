passwords = [
    {"service": "takeaway", "password": "asdf", "added_on": "21/03/22"},
    {"service": "takeaway", "password": "BINGO!", "added_on": "21/03/22"},
    {"service": "makersbnb", "password": "qwerty789", "added_on": "22/03/22"},
    {"service": "acebook", "password": "qwsdfdsfsdfsdfsd", "added_on": "22/03/22"},
]


# using the filter method
def is_acebook(password):
    return password["service"] == "acebook"


print(next(filter(is_acebook, passwords)))

# using a lambda (anonymous function) instead of the is_acebook function
print(next(filter(lambda password: password["service"] == "acebook", passwords)))


# practice v1
def are_all_passwords_long_enough(passwords):
    for password in passwords:
        if len(password["password"]) < 8:
            return False
    return True


print(are_all_passwords_long_enough(passwords))
# => false

# practice v2
# i) with calling a method)

# def is_too_short(pw):
#     return len(pw['password'] < 8)

# def are_all_passwords_long_enough(pw):
#     return len(list(filter(is_too_short, pw))) == 0

# are_all_passwords_long_enough(passwords)


# ii) with a lambda
# def are_all_passwords_long_enough(pw):
#     return len(list(filter(lambda password: len(password['password']), pw))) == 0

# are_all_passwords_long_enough(passwords)

# iii) with list comprehension


def are_all_passwords_long_enough(pw):
    return len([password for password in pw if len(password["password"]) < 8]) == 0


print(are_all_passwords_long_enough(passwords))


def was_pw_added_on(pw):
    return (
        len([password for password in pw if len(password["added_on"]) == "21/03/22"])
        == 0
    )


print(was_pw_added_on(passwords))


def list_of_date_added_on_220322(pw):
    pw_list = []
    for password in pw:
        if password["added_on"] == "21/03/22":
            pw_list.append(password["password"])

    return pw_list


print(list_of_date_added_on_220322(passwords))

result = map(lambda number: number * 2, [1, 2, 3, 4])

print(list(result))

print([number * 2 for number in [1, 2, 3, 4]])


def times_2(list):
    result = []
    for num in list:
        result.append(num * 2)
    return result


print(times_2([1, 2, 3, 4]))


def multiply_by_2(list):
    new_list = [num * 2 for num in list]
    return new_list


print(multiply_by_2([1, 2, 3, 4]))

# How to use for loops and if statements to search through a list ?

# for ele in list:
# if ele == 'whatever':
# do some thing

# How to use for loops to create a new list from an existing list
# def times_2(list):
# result = []
# for num in list:
#    result.append(num * 2)
# return result

#  Also using list comprehension:
#def multiply_by_2(list):
    # new_list = [num * 2 for num in list]
    # return new_list

# How filter and map can be an alternative to using for loops?
# Filter and Map are built in functions which can achieve commonly desired functionality of or a loops.
# ... using these enables one to write cleaner and more concise code.


# The difference between printing to the terminal and returning something ...?
# Returning some thing won't print any thing to the terminal. It ends the program and gives the result of the functionality at that stage,
# ... and will be the final result of the program. If nothing is returned, then the result of running the program has no value. However, 
# ... you can have a program print something as a result it's function, but it will have no return value.
#Printing will print the result of the program to the terminal.

# What is scope?

# Scope is on what level your program can be used, IE the scope of your program/data. It refers to visibility and accessibility.
# Local scope:
# Ie variables and functions inside a block. They are accessible only within that specific block and cannot be accessed outside of it.
# Local variables are created when the block is entered and destroyed when it is existed. 
# Global scope:
#Ie variables and functions outside a block. These are available through out the entire program.