pw = '1234567!'

def is_ok_length(password):
    return len(password) > 7

print(is_ok_length(pw))

def are_special_chars_included(password):
  if "!" in password:
    return True
  elif "@" in password:
    return True
  elif "$" in password:
    return True
  elif "%" in password:
    return True
  elif "&" in password:
    return True
  else:
    return False
  
print(are_special_chars_included(pw))

# def is_valid(password):
#   if is_ok_length(password) and are_special_chars_included(password):
#     return True
#   else:
#     return False 
  
def is_valid(password):
  return is_ok_length(password) and are_special_chars_included(password)

print(is_valid(pw))




