#it fails a test, will come back to this later.

def TreeConstructor(strArr):
  numbers = {}
  membership = {}
  counter = 0
  for item in strArr:
    print(item)
  for item in strArr:
    numbers[item[3]] = 1 + numbers.get(item[3], 0)
    membership[item[1]] = 1 + membership.get(item[1], 0)
  for key in membership:
    if(membership[key] > 1):
      return False
  for key in numbers:
    print(str(key) + " : " + str(numbers[key]))
  for key in numbers:
    if(numbers[key] > 2):
      return False
  return True

# keep this function call here 
print(TreeConstructor(input()))
