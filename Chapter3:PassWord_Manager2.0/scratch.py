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

class Person:
    def __init__(self, complex_dict):
        self.dict = complex_dict

    def get_work_address(self):
        work_address = f"{self.dict['addresses'][0]['building']} {self.dict['addresses'][0]['street']}"
        print(work_address)
        return work_address

    def get_home_address(self):
        home = self.dict['addresses'][1]
        return f"{home['building']} {home['street']}"

    # def get_pets(self):
    #     p = self.dict
    #     pets = p['pets']
    #     print(f"{p['name']} has {len(pets)} pets: a {pets[0]['animal']} called {pets[0]['name']}, a {pets[1]['animal']} called {pets[1]['name']}, a {pets[2]['animal']} called {pets[2]['name']}")
    #     return f"{p['name']} has {len(pets)} pets: a {pets[0]['animal']} called {pets[0]['name']}, a {pets[1]['animal']} called {pets[1]['name']}, a {pets[2]['animal']} called {pets[2]['name']}"


    def get_pets(self):
        pets = self.dict.get('pets', [])
        pets_summary = ", ".join([f"a {pet['animal']} called {pet['name']}" for pet in pets])
        return f"{self.dict['name']} has {len(pets)} pets: {pets_summary}"
    

person = Person({
        'name' : 'Alex',
    'pets' : [
    {'name' : 'Arthur', 'animal' : 'cat'},
    {'name' : 'Judith', 'animal' : 'dog'},
    {'name' : 'Gwen', 'animal' : 'goldfish'}
    ],
    'addresses' : [
    {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
    {'name' : 'home', 'building' : '10', 'street' : 'South Street'}
    ]
})

print(person.get_pets())

# password manager 2 planning

# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#      Add empty list instance variable

#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None

    # use password validator method from version 1
    # if pass word is valid, create a new dictionary of password and service name
    # 
    # check if password has been used before in another service
    # does the list include a dictionary with the same password as the argument?
    # add to list

    # need to refactor date time into a more manageable format
#    

#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None

    # Remove from list if list['service name] == argument  

#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None

    # use password validator again
    # password must be unique 
    # if list item [1]['service name'] == arg && password is valid ...
    # ... list item [0]['password'] = arg

#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password

    #  list comp? create new list of passwords - for loop?
        #  for x in list x[1].value ?
    #  or 

#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified

    #  takes two arguments (a, b)
    #  if a == 'service' return list in alphabetical order or order added?
    #  if a == 'added_on' return list accord to date
    #  if b == reverse, return a in reverse

#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists

    # filter x['service name'] == arg, x['password]
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.


from datetime import datetime
class PasswordManager2:
    def __init__(self):
        self.list = []
        self.arr = ["!", "@", "$", "%", "&"]

    def add(self, service, password):
        PwDict = {}
        ServiceDict = {}
        DateDict = {}
        for ele in self.list:
            if ele["password"] == password or ele["service"] == service:
                return

        for char in self.arr:
            if password.find(char) >= 0 and len(password) >= 8:
                now = datetime.now()
                ServiceDict["service"] = service
                PwDict["password"] = password
                DateDict['DateTime'] = str(now.date())
                ServiceDict.update(PwDict)
                ServiceDict.update(DateDict)

                self.list.append(ServiceDict)
        return self.list

    def remove(self, service):
        num = len(self.list) 
        for i in range(num):
            if self.list[i]["service"] == service:
                print([self.list[i]])
                print(i)
                del self.list[i]
                print(self.list)
        # return self.list

    def update(self, service, password):
        # for ele in self.list:
        #     if ele["password"] == password:
        #         return
        # newPW = ""

        # for char in self.arr:
        #     if password.find(char) >= 0 and len(password) >= 8:
        #         newPW = password

        # for ele in self.list:
        #     if ele["service"] == service and newPW == password:
        #         ele["password"] = newPW

        if any(ele['password'] == password for ele in self.list):
            return
        
        if any(char in password for char in self.arr) and len(password) >= 8:
            for ele in self.list:
                if ele["service"] == service:
                    ele["password"] = password
                break 

    def list_services(self):
        return [ele["service"] for ele in self.list]
    

    def sort_services_by(self, service, added_on, reverse):
        if service:
            return  [ele["service"] for ele in self.list]
        elif service and reverse:
            return  [ele["service"] for ele in self.list].reverse()
        elif added_on:
            sorted_data = sorted(self.list, key=lambda item: item["DateTime"])
            return sorted_data
        elif added_on and reverse:
            sorted_data = sorted(self.list, key=lambda item: item["DateTime"])
            return sorted_data.reverse()
        
    def get_for_service(self, service):
        for ele in self.list:
            if ele["service"] == service:
                return ele["password"]
            else:
                return None


pw = PasswordManager2()

pw.add("spaceX", "asdfxgh!!")
pw.add("spaceX", "ajgjgjgj!!!!")
pw.add("spaceX", "asdfxgh!!")


print(pw.add("nasa", "asdfxgh!!!!!!"))

print(pw.update("nasa", "hdhfhfhfhjkk!!"))
