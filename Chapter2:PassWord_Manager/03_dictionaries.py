tom = {
    "fav_food":"pizza",
    "fav_band": ["sabbath", 'Coltrane'],
     "favorite_programming_language": "Python"
}

capitals = {
    'england' : 'london',
    'spain' : 'madrid',
    'france' : 'paris',
    'ukraine' : 'kiev',
    'germany' : 'berlin'
}

print(tom['fav_food'])
print(tom['fav_band'][0])

person = {
    "name": "Jim Carrey",
    "nationality": ["Canadian", "American"],
    "favorite_programming_language": "Java"
  }

print(person['name'])
person["fav_colour"] = 'Black'
person['fav_food'] = 'pizza'
print(person)

print(person.keys())
# returns a list of keys
print(person.values())
#returns a list of values
print(person.get('fav_food'))
# gets value of key in ()
print(person.items())
# puts key:vals into an object as tuples. IE
#dict_items([('name', 'Jim Carrey'), ('nationality', ['Canadian', 'American']), 
# ('favorite_programming_language', 'Java'), ('fav_colour', 'Black'), ('fav_food', 'pizza')])
#dict_items[0][1]
# => Jim Carrey

print(person.pop('name'))
# => Jim Carrey
# prints value and removes key:value from dictionary
print(person)
# => {'nationality': ['Canadian', 'American'],
# ... 'favorite_programming_language': 'Java', 'fav_colour': 'Black', 'fav_food': 'pizza'}
person.clear()
#returns nothing but clears dictionary
print(person)
# => {}
person['c'] = 3
# setdefault(key, default)
print(person.setdefault('c', '3'))
print(person)

print(person.setdefault('name', 'tom'))
print(person)
# {'name': 'tom'}
# this retrieves the value of the key, but if that key doesn't exist it 
#gets created with default as the value
