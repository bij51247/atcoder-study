V,T,S,D = map(int,input().split())

t_distance = V*T
s_distance = V*S

if D < t_distance:
  print('Yes')
elif D >= t_distance and D <= s_distance:
  print('No')
else:
  print('Yes') 

#模範回答
# print('Yes' if (D < V*T or D > V* S) else 'No')