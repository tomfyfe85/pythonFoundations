# # def sort_by_last_letter(list):
# #     newList = [word[::-1] for word in list]
# #     newList.sort()
# #     finList = [word[::-1] for word in newList]
# #     return finList


# # print(sort_by_last_letter(["banana", "apple", "carrot", "avocado"]))


# # def greater_than_5(lis):
# #     return list(filter(lambda num: num > 5, lis))


# # print(greater_than_5([1, 6, 7, 5, 3, 2]))


# # def greater_than(lyst, num):
# #     newList = []
# #     for int in lyst:
# #         if int > num:
# #             newList.append(int)
# #     return newList


# # print(greater_than([9, 3, 6, 44, 7, 7], 6))


# # def less_than(lyst, num):
# #     newList = filter(lambda int: int < num, lyst)
# #     return list(newList)


# # print(less_than([9, 3, 6, 44, 1, 7, 7], 6))


# # def all_above(lyst, num):
# #     newList = list(map(lambda int: True if num < int else False, lyst))
# #     # return True if True in newList else False
# #     return list(newList)


# # print(all_above([9, 3, 6, 44, 1, 7, 7], 6))


# # def add_key_value_pair(dic, key, val):
# #     dic[key] = val
# #     return dic


# # def where_value_below(dic, num):
# #     newDic = {}
# #     for key, val in dic.items():
# #         if val < num:
# #             newDic[key] = val
# #     return newDic


# # print(where_value_below({"cat": 4, "person": 2, "centipede": 100}, 5))

# # # Class name: Greeter
# # # Purpose: say various greetings to a user with a given name
# # # Methods:
# # #   1. Name: hello
# # #      Arguments: one, a string representing a name
# # #      Returns: a string like 'Hello, NAME!'
# # #   2. Name: goodbye
# # #      Arguments: one, a string representing a name
# # #      Returns: a string like 'Goodbye, NAME!'
# # #   3. Name: good_night
# # #      Arguments: one, a string representing a name
# # #      Returns: a string like 'Good night, NAME!'
# # #   4. Name: good_morning
# # #      Arguments: one, a string representing a name
# # #      Returns: a string like 'Good morning, NAME!'
# # # Example usage:
# # #   > greeter = Greeter()
# # #   > greeter.hello('Bobby')
# # #   'Hello, Bobby!'
# # #   > greeter.goodbye('Bobby')
# # #   'Goodbye, Bobby!'
# # #   > greeter.good_night('Bobby')
# # #   'Good night, Bobby!'
# # #   > greeter.good_morning('Bobby')
# # #   'Good morning, Bobby!'


# # class Greeter:
# #     def hello(self, name):
# #         return f"Hello, {name}!"

# #     def goodbye(self, name):
# #         return f"Goodbye, {name}!"

# #     def good_night(self, name):
# #         return f"Good night, {name}!"

# #     def good_morning(self, name):
# #         return f"Good morning, {name}!"


# # # Class name: Basket
# # # Purpose: store a list of items
# # # Methods:
# # #   1. Name: __init__
# # #      Arguments: none
# # #   2. Name: add
# # #      Arguments: one item of any type
# # #      Returns: nothing
# # #   3. Name: list_items
# # #      Arguments: none
# # #      Returns: a list of all the items that have been added
# # # Example usage:
# # #   > basket = Basket()
# # #   > basket.add('apple')
# # #   > basket.add('banana')
# # #   > basket.add('orange')
# # #   > basket.list_items()
# # #   ['apple', 'banana', 'orange']


# # class Basket:
# #     def __init__(self):
# #         self.lyst = []

# #     def add(self, item):
# #         self.lyst.append(item)

# #     def list_items(self):
# #         return self.lyst


# # # Class name: Calculator
# # # Purpose: perform simple calculations and track the history
# # # Methods:
# # #   1. Name: __init__
# # #      Arguments: none
# # #   2. Name: add
# # #      Arguments: two numbers
# # #      Returns: the result of adding the two numbers
# # #   3. Name: multiply
# # #      Arguments: two numbers
# # #      Returns: the result of multiplying the first by the second
# # #   4. Name: subtract
# # #      Arguments: two numbers
# # #      Returns: the result of subtracting the second from the first
# # #   5. Name: divide
# # #      Arguments: two numbers
# # #      Returns: the result of dividing the first by the second
# # #   6. Name: list_history
# # #      Arguments: none
# # #      Returns: a list of all the previous results calculations
# # # Example usage:
# # #   > calculator = Calculator()
# # #   > calculator.add(1, 2)
# # #   3
# # #   > calculator.multiply(3, 4)
# # #   12
# # #   > calculator.subtract(5, 6)
# # #   -1
# # #   > calculator.divide(7, 8)
# # #   0.875
# # #   > calculator.list_history()
# # #   [3, 12, -1, 0.875]


# # class Calculator:
# #     def __init__(self):
# #         self.lyst = []

# #     def add(self, a, b):
# #         self.lyst.append(a + b)
# #         return self.lyst[0]

# #     def multiply(self, a, b):
# #         self.lyst.append(a * b)
# #         return self.lyst[0]

# #     def multiply(self, a, b):
# #         self.lyst.append(a * b)
# #         return self.lyst[0]

# #     def subtract(self, a, b):
# #         self.lyst.append(a - b)
# #         return self.lyst[0]

# #     def divide(self, a, b):
# #         self.lyst.append(a / b)
# #         return self.lyst[0]

# #     def list_history(self):
# #         return self.lyst


# # # Class name: Cohort
# # # Purpose: store a list of students
# # # Methods:
# # #   1. Name: __init__
# # #      Arguments: none
# # #      self.dikt = {}
# # #   2. Name: add_student
# # #      Arguments: one dictionary representing a student
# # #      Returns: nothing
# # #  self.dikt.update(student)

# # #   3. Name: list_students
# # #      Arguments: none
# # #      Returns: a list of all the students that have been added
# # #  return [self.dikt]

# # #   4. Name: list_employed_by
# # #      Arguments: one string, the name of an employer
# # #      Returns: a list of all the students who work for that employer
# # # filter through list for only students who have been employed by the arg
# # # filtered_List = filter(lambda student: for item in student: student[item] == arg, self.list )

# # # Example usage:
# # #   > cohort = Cohort()
# # #   > cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
# # #   > cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
# # #   > cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
# # #   > cohort.list_students()
# # #   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}, {'name' : 'Bobby', 'employer' : 'Google'}]
# # #   > cohort.list_employed_by('NASA')
# # #   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}]


# # def list_students(a):
# #     return [a]


# # print(list_students(13))


# # def list_employed_by(employer, lyst):
# #     # new = (list(filter(lambda student: student['employer'] == employer, lyst)))
# #     # return new
# #     # return [student for student in lyst if employer == student['employer']]

# #     # newList = []
# #     # for student in lyst:
# #     #     new = list(student.items())
# #     #     print(new)
# #     #     if new[1][1] == employer:
# #     #       newList.append(student)

# #     # return newList

# #     # return [list(student.items()) for student in lyst if student.get(') == employer]

# #     print(
# #         list_employed_by(
# #             "NASA",
# #             [
# #                 {"name": "Jo", "employer": "NASA"},
# #                 {"name": "Alex", "employer": "NASA"},
# #                 {"name": "Bobby", "employer": "Google"},
# #             ],
# #         )
# #     )


# # # Class name: Person
# # # Purpose: store a person's name, pets and addresses
# # # Methods:
# # #   1. Name: __init__
# # #      Arguments: one complex dictionary, see below for structure.
# # #   2. Name: get_work_address
# # #      Arguments: none
# # #      Returns: the work address in a nice format
# # #   3. Name: get_home_address
# # #      Arguments: none
# # #      Returns: the home address in a nice format
# # #   4. Name: get_pets
# # #      Arguments: none
# # #      Returns: a nice summary of the person's pets
# # # Example usage:
# # # > person = Person({
# # #     'name' : 'Alex',
# # #     'pets' : [
# # #       {'name' : 'Arthur', 'animal' : 'cat'},
# # #       {'name' : 'Judith', 'animal' : 'dog'},
# # #       {'name' : 'Gwen', 'animal' : 'goldfish'}
# # #     ],
# # #     'addresses' : [
# # #       {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
# # #       {'name' : 'home', 'building' : '10', 'street' : 'South Street'}
# # #     ]
# # #   })
# # #   > person.get_work_address()
# # #   '50 Commercial Street'
# # #   > person.get_home_address()
# # #   '10 South Street'
# # #   > person.get_pets()
# # #   'Alex has 3 pets: a cat called Arthur, a dog called Judith, a goldfish called Gwen'


# # class Person:
# #     def __init__(self, complex_dict):
# #         self.dict = complex_dict

# #     def get_work_address(self):
# #         work_address = f"{self.dict['addresses'][0]['building']} {self.dict['addresses'][0]['street']}"
# #         print(work_address)
# #         return work_address

# #     def get_home_address(self):
# #         home = self.dict["addresses"][1]
# #         return f"{home['building']} {home['street']}"

# #     # def get_pets(self):
# #     #     p = self.dict
# #     #     pets = p['pets']
# #     #     print(f"{p['name']} has {len(pets)} pets: a {pets[0]['animal']} called {pets[0]['name']}, a {pets[1]['animal']} called {pets[1]['name']}, a {pets[2]['animal']} called {pets[2]['name']}")
# #     #     return f"{p['name']} has {len(pets)} pets: a {pets[0]['animal']} called {pets[0]['name']}, a {pets[1]['animal']} called {pets[1]['name']}, a {pets[2]['animal']} called {pets[2]['name']}"

# #     def get_pets(self):
# #         pets = self.dict.get("pets", [])
# #         pets_summary = ", ".join(
# #             [f"a {pet['animal']} called {pet['name']}" for pet in pets]
# #         )
# #         return f"{self.dict['name']} has {len(pets)} pets: {pets_summary}"


# # person = Person(
# #     {
# #         "name": "Alex",
# #         "pets": [
# #             {"name": "Arthur", "animal": "cat"},
# #             {"name": "Judith", "animal": "dog"},
# #             {"name": "Gwen", "animal": "goldfish"},
# #         ],
# #         "addresses": [
# #             {"name": "work", "building": "50", "street": "Commercial Street"},
# #             {"name": "home", "building": "10", "street": "South Street"},
# #         ],
# #     }
# # )

# # print(person.get_pets())

# # # password manager 2 planning

# # # == INSTRUCTIONS ==
# # #
# # # Purpose: Manage a user's (valid) passwords
# # #
# # # Methods:
# # #   1. Name: __init__
# # #      Arguments: none
# # #      Add empty list instance variable

# # #   2. Name: add
# # #      Purpose: add a password for a service IF it is valid, otherwise do nothing
# # #      Arguments: one string representing a service name,
# # #                 one string representing a password
# # #      Returns: None

# # # use password validator method from version 1
# # # if pass word is valid, create a new dictionary of password and service name
# # #
# # # check if password has been used before in another service
# # # does the list include a dictionary with the same password as the argument?
# # # add to list

# # # need to refactor date time into a more manageable format
# # #

# # #   3. Name: remove
# # #      Purpose: remove a password for a service
# # #      Arguments: one string representing a service name
# # #      Returns: None

# # # Remove from list if list['service name] == argument

# # #   4. Name: update
# # #      Purpose: update a password for a service IF it is valid, otherwise do nothing
# # #      Arguments: one string representing a service name,
# # #                 one string representing a password
# # #      Returns: None

# # # use password validator again
# # # password must be unique
# # # if list item [1]['service name'] == arg && password is valid ...
# # # ... list item [0]['password'] = arg

# # #   5. Name: list_services
# # #      Arguments: none
# # #      Returns: a list of all the services for which the user has a password

# # #  list comp? create new list of passwords - for loop?
# # #  for x in list x[1].value ?
# # #  or

# # #   6. Name: sort_services_by
# # #      Arguments: A string, either 'service' or 'added_on',
# # #                 (Optional) A string 'reverse' to reverse the order
# # #      Returns: a list of all the services for which the user has a password
# # #               in the order specified

# # #  takes two arguments (a, b)
# # #  if a == 'service' return list in alphabetical order or order added?
# # #  if a == 'added_on' return list accord to date
# # #  if b == reverse, return a in reverse

# # #   7. Name: get_for_service
# # #      Arguments: one string representing a service name
# # #      Returns: the password for the given service, or None if none exists

# # # filter x['service name'] == arg, x['password]
# # #
# # # A reminder of the validity rules:
# # #   1. A password must be at least 8 characters long
# # #   2. A password must contain at least one of the following special characters:
# # #      `!`, `@`, `$`, `%` or `&`
# # #
# # # And a new rule: passwords must be unique (not reused in other services).
# # #
# # # Example usage:
# # #   > password_manager = PasswordManager2()
# # #   > password_manager.add('gmail', '12ab5!678')   # Valid password
# # #   > password_manager.add('facebook', '$abc1234') # Valid password
# # #   > password_manager.add('youtube', '3@245256')  # Valid password
# # #   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
# # #   > password_manager.get_for_service('facebook')
# # #   '$abc1234'
# # #   > password_manager.list_services()
# # #   ['gmail', 'facebook', 'youtube']
# # #   > password_manager.remove('facebook')
# # #   > password_manager.list_services()
# # #   ['gmail', 'youtube']
# # #   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
# # #   > password_manager.get_for_service('gmail')
# # #   '12ab5!678'
# # #   > password_manager.update('gmail', '%21321415')  # Valid password
# # #   > password_manager.get_for_service('gmail')
# # #   '%21321415'
# # #   > password_manager.sort_services_by('service')
# # #   ['gmail', 'youtube']
# # #   > password_manager.sort_services_by('added_on', 'reverse')
# # #   ['youtube', 'gmail']

# # # There are many more examples possible but the above should give you a good
# # # idea.


# # from datetime import datetime


# # class PasswordManager2:
# #     def __init__(self):
# #         self.list = []
# #         self.arr = ["!", "@", "$", "%", "&"]

# #     def add(self, service, password):
# #         PwDict = {}
# #         ServiceDict = {}
# #         DateDict = {}
# #         for ele in self.list:
# #             if ele["password"] == password or ele["service"] == service:
# #                 return

# #         for char in self.arr:
# #             if password.find(char) >= 0 and len(password) >= 8:
# #                 now = datetime.now()
# #                 ServiceDict["service"] = service
# #                 PwDict["password"] = password
# #                 DateDict["DateTime"] = str(now.date())
# #                 ServiceDict.update(PwDict)
# #                 ServiceDict.update(DateDict)

# #                 self.list.append(ServiceDict)
# #         return self.list

# #     def remove(self, service):
# #         num = len(self.list)
# #         for i in range(num):
# #             if self.list[i]["service"] == service:
# #                 print([self.list[i]])
# #                 print(i)
# #                 del self.list[i]
# #                 print(self.list)
# #         # return self.list

# #     def update(self, service, password):
# #         # for ele in self.list:
# #         #     if ele["password"] == password:
# #         #         return
# #         # newPW = ""

# #         # for char in self.arr:
# #         #     if password.find(char) >= 0 and len(password) >= 8:
# #         #         newPW = password

# #         # for ele in self.list:
# #         #     if ele["service"] == service and newPW == password:
# #         #         ele["password"] = newPW

# #         if any(ele["password"] == password for ele in self.list):
# #             return

# #         if any(char in password for char in self.arr) and len(password) >= 8:
# #             for ele in self.list:
# #                 if ele["service"] == service:
# #                     ele["password"] = password
# #                 break

# #     def list_services(self):
# #         return [ele["service"] for ele in self.list]

# #     def sort_services_by(self, service, added_on, reverse):
# #         if service:
# #             return [ele["service"] for ele in self.list]
# #         elif service and reverse:
# #             return [ele["service"] for ele in self.list].reverse()
# #         elif added_on:
# #             sorted_data = sorted(self.list, key=lambda item: item["DateTime"])
# #             return sorted_data
# #         elif added_on and reverse:
# #             sorted_data = sorted(self.list, key=lambda item: item["DateTime"])
# #             return sorted_data.reverse()

# #     def get_for_service(self, service):
# #         for ele in self.list:
# #             if ele["service"] == service:
# #                 return ele["password"]
# #             else:
# #                 return None


# # pw = PasswordManager2()

# # pw.add("spaceX", "asdfxgh!!")
# # pw.add("spaceX", "ajgjgjgj!!!!")
# # pw.add("spaceX", "asdfxgh!!")


# # print(pw.add("nasa", "asdfxgh!!!!!!"))

# # print(pw.update("nasa", "hdhfhfhfhjkk!!"))

# # import os


# # def does_file_exist(filename):
# #     if os.path.isfile("./" + filename) == True:
# #         print("hi")
# #         return True
# #     else:
# #         return False


# # print(does_file_exist("AirQuality.csv"))


# # import csv

# # file = open(
# #     "Users/tomfyfe/codes/makersProjects/python/pythonFoundationsMakersRepo/python_foundations/extension_challenges/01_files/program/AirQuality.csv"
# # )
# # print(file)


# # def get_file_contents(filename):
# #     if does_file_exist(filename):
# #         f = open("./AirQuality.csv")
# #         return f.readlines()
# #     else:
# #         return "This file cannot be found!"


# # # Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# # # boolean argument "include_header_row" is True, return the first header row
# # # from the filename as well (if it is False, omit that row)
# # # Example:
# # #   Call: christmas_day_air_quality("AirQuality.csv", True)
# # #   Returns:
# # #     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
# # #     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
# # #     [...]
# # #   Call: christmas_day_air_quality("AirQuality.csv", False)
# # #   Returns:
# # #     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
# # #     [...]
# # # Notes:
# # # * should use get_file_contents() - N.B. as should any subsequent
# # # functions you write, using anything previously built if and where necessary

# # # get header into a list
# # # use get_file_contents
# # # is header 0 indexed element?
# # # is each line one element and data in the element is separated by ;
# # # if True loop through data list and append elements beginning with '25'
# # #  ... to the list with the header and return

# # # if false then filter data list by elements starting with '25'


# # def christmas_day_air_quality(filename, include_header_row):
# #     if include_header_row == True:
# #         newList = []
# #         f = get_file_contents(filename)
# #         newList.append(f[0])
# #         print(newList)
# #         print("true")

# #         for ele in f:
# #             if ele[:10] == "25/12/2004":
# #                 newList.append(ele)
# #         print("newList")
# #         # print(newList)
# #         return newList

# #     else:
# #         falseList = []
# #         print("false")
# #         q = get_file_contents(filename)
# #         print(q)
# #         for ele in q:
# #             if ele[:10] == "25/12/2004":
# #                 falseList.append(ele)
# #             print(falseList)
# #         return falseList


# # # REFACTORED


# # def christmas_day_air_quality(filename, include_header_row):
# #     f = get_file_contents(filename)
# #     newList = [ele for ele in f if ele[:10] == "25/12/2004"]

# #     if include_header_row:
# #         newList.insert(0, f[0])

# #     return newList


# # # Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# # # Example:
# # #   Call: christmas_day_average_air_quality("AirQuality.csv")
# # #   Returns: 1439.21
# # # Data sample:
# # # Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# # # 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;

# # # divide the sum of every forth number in each element by the number of elements ??
# # # Use get_file_content to get the list
# # # split(';') each element
# # # get 4th element of each new array,
# # # a method... += each result of get 4th element of each new array,
# # # b method... keep count of iterations with a counter
# # # get result by a/b


# # def christmas_day_average_air_quality(filename):
# #     f = get_file_contents(filename)
# #     f.pop(0)
# #     counter = 1
# #     sumOfAirQuality = 0
# #     for ele in f:
# #         print(counter)
# #         newList = ele.split(";")

# #         print(newList)
# #         if newList[3] != "":
# #             print(newList[3])
# #             counter += 1

# #             num = round(float(newList[3]), 2)
# #             sumOfAirQuality += num
# #         print(sumOfAirQuality / counter)

# #     return sumOfAirQuality / counter


# # # Purpose: scrape all the data and calculate average values for each of the 12 months
# # #          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
# # #          representations of months and values as the averages (to 2 decimal places)
# # # Example:
# # #   Call: get_averages_for_month("AirQuality.csv")
# # #   Returns: {1: 1003.47, [...], 12: 948.71}
# # # Notes:
# # # * Data from months across multiple years should all be averaged together
# # def get_averages_for_month(filename):
# #     f = get_file_contents(filename)
# #     newDict = {}
# #     counter = 0
# #     sum = 0
# #     counter2 = 0
# #     sum2 = 0
# #     counter3 = 0
# #     sum3 = 0

# #     for ele in f:
# #         newList = ele.split(";")
# #         nL = newList[0][3:5]
# #         if nL == "01":
# #             counter += 1
# #             sum += int(newList[3])
# #             av = sum / counter
# #             newDict[1] = round(float(av), 2)

# #         elif nL == "03":
# #             counter2 += 1
# #             sum2 += int(newList[3])
# #             av2 = sum2 / counter2
# #             newDict[3] = round(float(av2), 2)

# #         elif nL == "04":
# #             newDict[2] = "2"
# #             for x in range(4, 11):
# #                 newDict[x] = f"{x}"

# #         elif nL == "12":
# #             counter3 += 1
# #             sum3 += int(newList[3])
# #             av = sum3 / counter3
# #             newDict[12] = round(float(av), 2)

# #         else:
# #             None

# #     new = dict(sorted(newDict.items()))
# #     # print(new[1])
# #     return new


# # # more pythonic way:


# # def get_averages_for_month(filename):
# #     f = get_file_contents(filename)
# #     f.pop(0)

# #     monthly_sum = [0] * 13
# #     # Initialize lists to store cumulative sums and counts for each month
# #     monthly_count = [0] * 13
# #     # [0,0,0,0,0,0,0,0,0,0,0,0,0] Index 0 wont be used

# #     finalDict = {}
# #     for ele in f:
# #         newList = ele.split(";")
# #         # print(newList[9300])
# #         if newList[0][3:5] != "":
# #             month = int(newList[0][3:5])
# #             # print(f'current month {month}')
# #             value = int(newList[3])
# #             # print(f'current value = {value}')
# #             monthly_sum[month] += value
# #             # print(f'current month and sum of value: month- {month}, sum- {value}')
# #             monthly_count[month] += 1
# #             # print(f'reports per month in 0 index {monthly_count}')
# #             # print(month)
# #             # print(round(monthly_sum[month]/monthly_count[month], 2))
# #             average = round(monthly_sum[month] / monthly_count[month], 2)
# #             finalDict[month] = average

# #     return finalDict


# # Purpose: write only the rows relating to March (any year) to a new file, in the same
# # location as the original, including the header row of labels
# # Example
# #   Call: create_march_data("AirQuality.csv")
# #   Returns: nothing, but writes header + March data to file called
# #            "AirQualityMarch.csv" in same directory as "AirQuality.csv"

# #  look up how to create a new file in a function and save it to a directory
# #  csv.writer -  This function writes the data to a CSV file.

# # use get_file_contents
# # create empty list
# # iterate through f and .split(';') each element and if newList[0][3:5] == '3' or newList[0][:4] == "Date"
# # add to empty list
# #
# # create csv file in the same directory as AirQuality.csv and save list to new csv file
# # import csv

# # def create_march_data(filename):
# #     f = get_file_contents(filename)
# #     dataList = []
# #     for ele in f:
# #         newList = ele.split(";")
# #         if newList[0][:4] == "Date" or newList[0][3:5] == "03":
# #             dataList.append(newList[0:5])

# #     filePath = "/Users/tomfyfe/codes/makersProjects/python/pythonFoundationsMakersRepo/python_foundations/extension_challenges/01_files/program/AirQualityMarch.csv"

# #     with open("AirQualityMarch.csv", "w", newline="") as f:
# #         writer = csv.writer(f, delimiter=";")
# #         writer.writerows(dataList)

#     # Purpose: write monthly responses files to a new directory called "monthly_responses",
#     # in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
#     # including the header row of labels in each one.
#     # Example
#     #   Call: create_monthly_responses("AirQuality.csv")
#     #   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#     #            data matching responses from that month and year

#     # create a new directory from within the function called "monthly_responses",
#     # create a file for each month in each year
#     # each file will contain all the info for that month, in that year

#     # file name should be EG 07-2004.csv
#     #  => "/monthly_responses/07-2004.csv"

#     # find out how to create a file named after info given in a list
#     # if dates in list of info match file name, add to file as above

#     # perhaps loop though AirQuality.csv to create files to directory
#     # loop through AirQuality.csv and if dates match, add to specific file


# def create_monthly_responses(filename):
#     f = get_file_contents(filename)
#     header = f.pop(0)

#     folder_path = "/Users/tomfyfe/codes/makersProjects/python/pythonFoundationsMakersRepo/python_foundations/extension_challenges/01_files/program/monthly_responses/"
#     os.mkdir(folder_path)
#     dataList = []

#     for ele in f:
#         newList = ele.split(";")
#         # print(newList[0][3:10])
#         if newList[0] != "":
#             month = newList[0][3:5]
#             year = newList[0][6:10]
#             # print( int(monthAndDate[0:2]))
#             # print(newList[0:-2])
#             dataList.append(newList[0:-2])
#             # print(dataList[-1][0][3:10])

#             if  dataList[-1][0][3:10] == newList[0][3:10]:
#                 print(newList)
#                 filePath = folder_path + f"{month}-{year}.csv"
#                 with open(filePath, "w", newline="") as f:
#                     writer = csv.writer(f, delimiter=";")
#                     writer.writerows(dataList)
#             else:
#                 dataList = []
#                 # dataList.append(newList[0:-2])

#     # print(dataList)

#     # all data up to the end of the month that the file is named after is being entered into the files. IE 05-2004 has all 2004 months (expect 01/02) entered,
#     # but no more. Interestingly, months 1 and 2 only appear in their folders and the bottom of the file, like the other files, however 01 and 02 aren't present in other files.

#     #  plan1 - Use conditional to only append the next iteration if the data matches the date of the last element of the list, else list =[]
#     #  plan2 - Use conditional as above, but make a new list or for each month and store in a main list. There should be an individual nested list
#     # ... for each month. Now iterate though in a new loop, each time creating a new file etc and adding the data for each month.

#     # each file contain all info for every month
#     # ON THE RIGHT TRACK THOUGH!

from urllib.request import urlopen
import json



url = urlopen("https://jsonplaceholder.typicode.com/users")
# response = url.read().decode('UTF-8')
# json_data = json.loads(response)
# print(json_data['current_weather'])


def load_data_from_url(url):
    file = urlopen(url)
    response = file.read().decode("UTF-8")
    json_data = json.loads(response)
    return json_data


print(load_data_from_url("https://jsonplaceholder.typicode.com/users"))
