# Option 1: Add another key value pair for each service
{
  'acebook_password' : 'password123',
  'acebook_added' : '22/03/22',
  'makersbnb_password' : 'qwerty789',
  'makersbnb_added' : '22/03/22'
}

# Option 2: Convert to a nested dictionary
{
  'acebook' : {
    'password' : 'password123',
    'added_on' : '22/03/22',
  },
  'makersbnb' : {
    'password' : 'qwerty789',
    'added_on' : '22/03/22',
  }
}

# Option 3: Convert to a list of dictionaries
[
  {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},
  {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'}
]

>>> passwords = {
>>>  'acebook_password' : 'password123',
>>>  'acebook_added' : '22/03/22',
>>>  'makersbnb_password' : 'qwerty789',
>>>  'makersbnb_added' : '22/03/22'
>>> }
>>> # first we get the password
>>> passwords['acebook_password']
'password123'
>>> # then we get the date on which it was added
>>> passwords['acebook_added']
'22/03/22'

>>> passwords = {
...   'acebook' : {
...     'password' : 'password123',
...     'added_on' : '22/03/22',
...   },
...   'makersbnb' : {
...     'password' : 'qwerty789',
...     'added_on' : '22/03/22',
...   }
...  }
> passwords['acebook']
: {'password' : 'password123', 'added_on' : '22/03/22'}

>>> passwords = [  {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},  {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'} ]
>>> def find(service):
...     for pwd in passwords:
...             if pwd['service'] == service:
...                     return pwd
... 
>>> find("acebook")
{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'}

# I choose option 2 as i think it is easier to read
# and requires no loop to find key. Also, dictionaries can be
# converted into lists if needed.

