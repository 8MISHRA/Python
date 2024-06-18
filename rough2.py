def to_centigrade(n):
	return 5*(n-32) / 9

fun = to_centigrade
to_centigrade = 9
a = fun (100)
print(a)