def dec2bin(list):
  sum,st = 0,0
  for num in list:
    sum += num*2**st
    st += 1
  return sum
