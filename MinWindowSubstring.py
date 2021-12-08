def MinWindowSubstring(strArr):
  #strArr contains the main string and substring.
  bigOne = strArr[0]
  littleOne = strArr[1]
  countTable, window = {}, {}
  #if non existing, set it as 0
  for c in littleOne:
    countTable[c] = 1 + countTable.get(c, 0)
  have, need = 0, len(countTable)
  result, resultLen = [-1, -1], sys.maxint
  #left pointer
  l = 0
  #right pointer
  for r in range(len(bigOne)):
    c = bigOne[r]
    window[c] = 1 + window.get(c, 0)
    if c in countTable and window[c] == countTable[c]:
      have += 1
    
    while have == need:
      if(r - l + 1) < resultLen:
        result = [l, r]
        resultLen = (r - l + 1)
      window[bigOne[l]] -= 1
      if bigOne[l] in countTable and window[bigOne[l]] < countTable[bigOne[l]]:
        have -= 1
      l += 1
  l, r = result
  # code goes here
  return bigOne[l:r + 1]

# keep this function call here 
print(MinWindowSubstring(input()))
