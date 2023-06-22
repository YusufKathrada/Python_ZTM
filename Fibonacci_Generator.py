#Create a function that takes the index of the fibonacci sequence and dislays the sequenece until that index

# Using Generators
def fib(num):
  a = 0
  b = 1
  for i in range(num):
    yield a
    temp = a
    a = b
    b = temp + b

for x in fib(21):
  print(x)

Using list
def fib2(num):
  a = 0
  b = 1
  result = []
  for i in range(num):
    result.append(a)
    temp = a
    a = b
    b = temp + b
  return result

print(fib2(21))
