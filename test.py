def dec2bin(list):
  sum,step = 0,0
  for num in list:
    sum += num*2**step
    step += 1
  return sum
