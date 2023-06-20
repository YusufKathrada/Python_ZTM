# Create an @authenticated decorator that only allows the function to run if user has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'Steven',
    'valid': False
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
      return fn(*args, **kwargs)
    else:
      print('user not authenticated')
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
message_friends(user2)
