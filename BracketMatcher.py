def BracketMatcher(strParam):
  lb, rb = "(", ")"
  stack = []
  if(strParam[0] == rb):
    return 0

  for i in range(len(strParam)):
    if(strParam[i] == lb):
      stack.append(lb)
    elif(strParam[i] == rb):
      if len(stack) > 0 and stack[len(stack) - 1] == lb:
        stack.pop()
      else:
        return 0
  if(len(stack) == 0):
    return 1
  else:
    return 0
  

# keep this function call here 
print(BracketMatcher(input()))
