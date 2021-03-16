x,y = map(int,input().split())

if x > y:
  dominace = x
  inferior = y
else:
  dominace = y
  inferior = x

if (dominace - inferior <= 2):
  print('Yes')
else:
  print('No')
  
  
# x, y = map(int, input().split())
# print('Yes' if min(x, y) + 3 > max(x, y) else 'No')