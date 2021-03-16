#A:無脂乳固形 B:乳脂肪分 
A,B = map(int,input().split())

#A+B=乳固形

if A+B >= 15 and B >=8:
  print(1)
elif A+B >= 10 and B>=3:
  print(2)
elif A+B >= 3:
  print(3)
else: 
  print(4)
  