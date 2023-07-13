class Greeter():
    def hello(self):
        return 'Hello'
   
    def bye(self):
        return 'Bye'

greet = Greeter()
print(greet)
greet.hello()
print(greet.hello())
print(greet.bye())

class Asker():
    def __init__(self):
        print('are you ok?')

ask = Asker()

class Person():
    def __init__(self, name, birthday, favourite_language):
        self.name = name
        self.birthday = birthday
        self.favourite_language = favourite_language

person1 = Person("Alan Turing", "June 23, 1912", "Standard Description")

print(person1.name)
print(person1.birthday)

class SuperVillain():
    def __init__(self, name, arch, skill):
        self.name = name
        self.arch = arch
        self.skill = skill

vil = SuperVillain('Joker', 'Batman', 'Insanity')

print(vil.name)
print(vil.arch)
print(vil.skill)

class Greeter2():
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        return f"oh HELLO {self.name}!"
    
greeter2 = Greeter2('Allan')
print(greeter2.hello())

class Person():
# note that we're not using instance variables here
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname

    def full_name(self):
    # will this work without using instance variables above?
        return f"{self.first_name} {self.surname}"

alan_turing = Person("Alan", "Turing")
print(alan_turing.full_name())