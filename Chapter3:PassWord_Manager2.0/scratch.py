def sort_by_last_letter(list):
    newList = [word[::-1] for word in list]
    newList.sort()
    finList = [word[::-1] for word in newList]
    return finList


print(sort_by_last_letter(["banana", "apple", "carrot", "avocado"]))


def greater_than_5(lis):
    return list(filter(lambda num: num > 5, lis))


print(greater_than_5([1, 6, 7, 5, 3, 2]))


def greater_than(lyst, num):
    newList = []
    for int in lyst:
        if int > num:
            newList.append(int)
    return newList


print(greater_than([9, 3, 6, 44, 7, 7], 6))

def less_than(lyst, num):
  newList = filter(lambda int: int < num, lyst)
  return list(newList)

print(less_than([9, 3, 6, 44, 1, 7, 7], 6))

def all_above(lyst, num):
    newList = list(map(lambda int: True if num < int else False, lyst))
    # return True if True in newList else False
    return list(newList)

print(all_above([9, 3, 6, 44, 1, 7, 7], 6))

def add_key_value_pair(dic, key, val):
    dic[key] = val
    return dic

def where_value_below(dic, num):
    newDic = {}
    for key, val in dic.items():
        if val < num:
            newDic[key] = val
    return newDic

print(where_value_below({'cat': 4, 'person': 2, 'centipede': 100}, 5))

# Class name: Greeter
# Purpose: say various greetings to a user with a given name
# Methods:
#   1. Name: hello
#      Arguments: one, a string representing a name
#      Returns: a string like 'Hello, NAME!'
#   2. Name: goodbye
#      Arguments: one, a string representing a name
#      Returns: a string like 'Goodbye, NAME!'
#   3. Name: good_night
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good night, NAME!'
#   4. Name: good_morning
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good morning, NAME!'
# Example usage:
#   > greeter = Greeter()
#   > greeter.hello('Bobby')
#   'Hello, Bobby!'
#   > greeter.goodbye('Bobby')
#   'Goodbye, Bobby!'
#   > greeter.good_night('Bobby')
#   'Good night, Bobby!'
#   > greeter.good_morning('Bobby')
#   'Good morning, Bobby!'

class Greeter():
    def hello(self, name):
        return f"Hello, {name}!"
    
    def goodbye(self, name):
        return f"Goodbye, {name}!"
    
    def good_night(self, name):
        return f"Good night, {name}!"
    
    def good_morning(self, name):
        return f"Good morning, {name}!"
    
# Class name: Basket
# Purpose: store a list of items
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: one item of any type
#      Returns: nothing
#   3. Name: list_items
#      Arguments: none
#      Returns: a list of all the items that have been added
# Example usage:
#   > basket = Basket()
#   > basket.add('apple')
#   > basket.add('banana')
#   > basket.add('orange')
#   > basket.list_items()
#   ['apple', 'banana', 'orange']
    
class Basket():
    def __init__(self): 
        self.lyst = []
    
    def add(self, item):
        self.lyst.append(item)

    def list_items(self):
        return self.lyst


# Class name: Calculator
# Purpose: perform simple calculations and track the history
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: two numbers
#      Returns: the result of adding the two numbers
#   3. Name: multiply
#      Arguments: two numbers
#      Returns: the result of multiplying the first by the second
#   4. Name: subtract
#      Arguments: two numbers
#      Returns: the result of subtracting the second from the first
#   5. Name: divide
#      Arguments: two numbers
#      Returns: the result of dividing the first by the second
#   6. Name: list_history
#      Arguments: none
#      Returns: a list of all the previous results calculations
# Example usage:
#   > calculator = Calculator()
#   > calculator.add(1, 2)
#   3
#   > calculator.multiply(3, 4)
#   12
#   > calculator.subtract(5, 6)
#   -1
#   > calculator.divide(7, 8)
#   0.875
#   > calculator.list_history()
#   [3, 12, -1, 0.875]

class Calculator():
    def __init__(self):
        self.lyst = []

    def add(self, a, b):
        self.lyst.append(a + b)
        return self.lyst[0]
    
    def multiply(self, a, b):
        self.lyst.append(a * b)
        return self.lyst[0]
    
    def multiply(self, a, b):
        self.lyst.append(a * b)
        return self.lyst[0]
    
    def subtract(self, a, b):
        self.lyst.append(a - b)
        return self.lyst[0]

    def divide(self, a, b):
        self.lyst.append(a/b)
        return self.lyst[0]
    
    def list_history(self):
        return self.lyst