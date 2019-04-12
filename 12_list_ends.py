import numpy as np
a = np.random.randint(20, size = 10)
def list_ends(a):
  return [a[0], a[-1]]
print(list_ends(a))
