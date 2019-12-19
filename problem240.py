import math
max_perms = math.factorial(20)

# run = number of previous rolls of the same value
# div = factor by which to reduce dice permutations to avoid double counting
def f(num_dice, num_summed, max_value, value_sum, div=1, run=0):

  if num_dice == 0:
    return round(max_perms / div)
  
  total = 0
  it = range(1, max_value+1)
  if num_summed > 0:
    it = range(math.ceil(value_sum/num_summed), min(value_sum-num_summed+2,max_value+1))
  for val in it:       
    if val == max_value:
      total += f(num_dice-1, num_summed-1, val, value_sum-val, div = div*(run+1), run = run+1)
    else:
      total += f(num_dice-1, num_summed-1, val, value_sum-val, div = div)
    
  return total

print(f(20, 10, 12, 70))


