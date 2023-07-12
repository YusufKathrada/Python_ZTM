# Password validator

# password must be 8 char long
# can contain letters, numbers and $%#@
# must end with a number
import re

# Found using regex101.com
regex = re.compile(r"[a-zA-Z0-9$%#@]{7,}\d")



while True:
  user_passsword = input("Please enter your password: \n")

  check = regex.fullmatch(user_passsword)
  if check != None:
    print("Password Successful!")
    break
  else:
    print("Password does not meet criteria. Please try again")
