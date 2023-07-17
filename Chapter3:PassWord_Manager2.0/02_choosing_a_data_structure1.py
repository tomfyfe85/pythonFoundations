# The current data structure
{
  'acebook' : 'password123',
  'makersbnb' : 'qwerty789'
}

# Option 1: Add another key value pair for each service
{
  'acebook_password' : 'password123',
  'acebook_added' : '22/03/22',
  'makersbnb_password' : 'qwerty789',
  'makersbnb_added' : '22/03/22'
}

# Option 2: A nested dictionary
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

# Option 3: A list of dictionaries
[
  {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},
  {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'}
]