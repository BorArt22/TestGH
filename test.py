def dec2bin(list):
  sum,st = 0,0
  for a in list:
    sum += a*2**st
    st += 1
  return sum
