output = -1

def issquare(n):
    	return int(n ** 0.5) ** 2 == n

n, m = map(int, input().split())
table =  [list(input().strip()) for x in range(n)]


for i in range(n):
      for j in range(m):
            for row in range(-n, n):
                  for col in range(-m, m):
                        if row == 0 and col == 0:
                              continue
                        temp = ""
                        x, y = i, j
                        while 0 <= x < n and 0 <= y < m:
                              temp += table[x][y]
                              if issquare(int(temp)):
                                    output = max(output, int(temp))
                              x += row
                              y += col
print(output)