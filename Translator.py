# create an app that reds from a text file and translates it
from translate import Translator
# pip install translate

translator = Translator(to_lang='ja')

try:
  with open('Text.txt') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)

except FileNotFoundError as e:
  print("File not found")
  raise e
