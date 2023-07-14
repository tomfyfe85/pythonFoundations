# class Greeter():
#     def hello(self):
#         return 'Hello'
   
#     def bye(self):
#         return 'Bye'

# greet = Greeter()
# print(greet)
# greet.hello()
# print(greet.hello())
# print(greet.bye())

# class Asker():
#     def __init__(self):
#         print('are you ok?')

# ask = Asker()

# class Person():
#     def __init__(self, name, birthday, favourite_language):
#         self.name = name
#         self.birthday = birthday
#         self.favourite_language = favourite_language

# person1 = Person("Alan Turing", "June 23, 1912", "Standard Description")

# print(person1.name)
# print(person1.birthday)

# class SuperVillain():
#     def __init__(self, name, arch, skill):
#         self.name = name
#         self.arch = arch
#         self.skill = skill

# vil = SuperVillain('Joker', 'Batman', 'Insanity')

# print(vil.name)
# print(vil.arch)
# print(vil.skill)

# class Greeter2():
#     def __init__(self, name):
#         self.name = name
    
#     def hello(self):
#         return f"oh HELLO {self.name}!"
    
# greeter2 = Greeter2('Allan')
# print(greeter2.hello())

# class Person():
# # note that we're not using instance variables here
#     def __init__(self, first_name, surname):
#         self.first_name = first_name
#         self.surname = surname

#     def full_name(self):
#     # will this work without using instance variables above?
#         return f"{self.first_name} {self.surname}"

# alan_turing = Person("Alan", "Turing")
# print(alan_turing.full_name())

# Class name: Cohort
# Purpose: represents a cohort
# Fields:
#   1. Name: name
#      Type: string
#      Purpose: the cohort name
#   2. Name: start_date
#      Type: Date
#      Purpose: the cohort start date
#   3. Name: end_date
#      Type: Date
#      Purpose: the cohort end date
# Methods:
#   1. Name: __init__
#      Arguments: one string representing a name,
#                 one string representing a start_date,
#                 one string representing an end_date
#   2. Name: calculate_duration
#      Arguments: none
#      Returns: the number of days between start_date and end_date
# Example usage:
#   > cohort = Cohort('June 2020', '2020-06-01', '2020-09-01')
#   > cohort.name
#   'June 2020'
#   > cohort.start_date
#   datetime.date(2020, 6, 1)
#   > cohort.end_date
#   datetime.date(2020, 9, 1)
#   > cohort.calculate_duration()
#   92
from datetime import datetime
from datetime import date
class Cohort():
    def __init__(self, name, start_date, end_date):
                resStart = tuple(map(int, start_date.split('-')))
                resEnd = tuple(map(int, end_date.split('-')))
                self.name = name
                # self.start_date = date(datetime.datetime.strptime(start_date, format))
                self.start_date = date(*resStart)
                self.end_date = date(*resEnd)
                

    def calculate_duration(self):
        sum = self.end_date - self.start_date
        
        print('sum')
        print(sum.days)
        print(type(sum))
        days = sum.days
        string = str(days)
        print(len(string))
        
        fin = int(string)
        print(type(fin))
        return fin



cohort = Cohort('June 2020', '2020-05-01', '2790-05-01')
# #   > cohort.name
# print(type(cohort.start_date))
# print(cohort.start_date)
print(cohort.calculate_duration())
