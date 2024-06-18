# [x * x for x in range(1, 11)]

# nums = [-1, 25, 9, -30, 5]
# pos = [x for x in nums if x > 0]
# sqneg = [x * x for x in nums if x < 0]
# abspair = [(x, abs(x)) for x in nums]
# p = [(x, y) for x in nums for y in [1, 2, 3, 4, 625, 900] if x*x == y]

# print(p)
# print(abspair)
# print(pos)
# print(sqneg)

for x in range (1, 4):
	for y in range (5, 8):
		for z in range (1, 9):
			print((x, y, z))