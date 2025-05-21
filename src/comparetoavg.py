def compareToAvg(a, b, c, avg): 
  """
  Prints whether each number is below, equal to, or above the average.
  """
for val in [a, b, c]: 
  if val < avg:
    print(f'{val} is less than the average {avg}')
  elif val > avg: 
    print(f'{val} is greater than the average {avg}')
  else: 
    print(f'{val} is equal to the {avg}')
