a,b = input().split()

a_list = list(a)
b_list = list(b)

a_numlist = [int(i) for i in list(a_list)]
b_numlist = [int(i) for i in list(b_list)]

a_sum = 0
b_sum = 0
for a in a_numlist:
  a_sum += a
for b in b_numlist:
  b_sum += b

if a_sum > b_sum:
  print(a_sum)
else:
  print(b_sum)

# A, B = input().split()
# A = int(A[0]) + int(A[1]) + int(A[2])
# B = int(B[0]) + int(B[1]) + int(B[2])
# print(max(A, B))