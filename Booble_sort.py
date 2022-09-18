a = [33, 24, 91, 69, 79, 111, 22, 2]
n = len(a)

for i in range(n-1):
  m = i
  for j in range(i+1, n):
    if a[i] > a[j]:
      m = j
  a[i], a[m] = a[m], a[i]
  
print(a)