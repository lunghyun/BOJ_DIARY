tCase = int(input()) 
output = ""
for i in range(tCase):
  x, y = map(int, input().split())
  d = y - x
  n = 0
  while True:
    if d <= n*(n+1):
      break
    n += 1
  if d <= n**2:
    output += str(n*2-1)
  else:
    output += str(n*2)

  output += "\n"
print(output)