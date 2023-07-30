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


print(where_value_below({"cat": 4, "person": 2, "centipede": 100}, 5))

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


class Greeter:
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


class Basket:
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


class Calculator:
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
        self.lyst.append(a / b)
        return self.lyst[0]

    def list_history(self):
        return self.lyst


# Class name: Cohort
# Purpose: store a list of students
# Methods:
#   1. Name: __init__
#      Arguments: none
#      self.dikt = {}
#   2. Name: add_student
#      Arguments: one dictionary representing a student
#      Returns: nothing
#  self.dikt.update(student)

#   3. Name: list_students
#      Arguments: none
#      Returns: a list of all the students that have been added
#  return [self.dikt]

#   4. Name: list_employed_by
#      Arguments: one string, the name of an employer
#      Returns: a list of all the students who work for that employer
# filter through list for only students who have been employed by the arg
# filtered_List = filter(lambda student: for item in student: student[item] == arg, self.list )
    
# Example usage:
#   > cohort = Cohort()
#   > cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
#   > cohort.list_students()
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}, {'name' : 'Bobby', 'employer' : 'Google'}]
#   > cohort.list_employed_by('NASA')
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}]


def list_students(a):
    return [a]

print(list_students(13))

def list_employed_by(employer, lyst):
    # new = (list(filter(lambda student: student['employer'] == employer, lyst)))
    # return new
    # return [student for student in lyst if employer == student['employer']]
  
  # newList = []
  # for student in lyst:
  #     new = list(student.items())
  #     print(new)
  #     if new[1][1] == employer:
  #       newList.append(student)

  # return newList

    # return [list(student.items()) for student in lyst if student.get(') == employer]


  print(list_employed_by('NASA', [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}, {'name' : 'Bobby', 'employer' : 'Google'}]))

# Class name: Person
# Purpose: store a person's name, pets and addresses
# Methods:
#   1. Name: __init__
#      Arguments: one complex dictionary, see below for structure.
#   2. Name: get_work_address
#      Arguments: none
#      Returns: the work address in a nice format
#   3. Name: get_home_address
#      Arguments: none
#      Returns: the home address in a nice format
#   4. Name: get_pets
#      Arguments: none
#      Returns: a nice summary of the person's pets
# Example usage:
  # > person = Person({
  #     'name' : 'Alex',
  #     'pets' : [
  #       {'name' : 'Arthur', 'animal' : 'cat'},
  #       {'name' : 'Judith', 'animal' : 'dog'},
  #       {'name' : 'Gwen', 'animal' : 'goldfish'}
  #     ],
  #     'addresses' : [
  #       {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
  #       {'name' : 'home', 'building' : '10', 'street' : 'South Street'}
  #     ]
  #   })
#   > person.get_work_address()
#   '50 Commercial Street'
#   > person.get_home_address()
#   '10 South Street'
#   > person.get_pets()
#   'Alex has 3 pets: a cat called Arthur, a dog called Judith, a goldfish called Gwen'

