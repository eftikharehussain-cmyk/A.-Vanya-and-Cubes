# A.-Vanya-and-Cubes
n = int(input())
lst = []
count = 0
i = 1
count1 = 0
while sum(lst) < n:
	count += i
	i += 1
	count1 += 1
	lst.append(count)
if sum(lst) > n:
	count1 -= 1
print(count1)
