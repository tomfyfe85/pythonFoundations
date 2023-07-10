def add(a, b):
    return a + b


def add3(a, b, c):
    return a + b + c


def seconds_In_A_Week(x):
    seconds = x * 604800
    return f"there are {seconds} seconds in {x} week's"


def superify(name):
    return f"super{name}"


dog_result = superify("dog")
print(f"Look, it's {dog_result}!")

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}")


print(add(1, 2))
print(add3(1, 2, 3))
print(seconds_In_A_Week(3))
