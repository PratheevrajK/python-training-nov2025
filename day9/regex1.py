import re

pat = r"Rs.[0-9]{2,3}"
l2 = "The orange costs Rs.23 and Grapes costs Rs.670, total is Rs.123456."
result = re.fullmatch(pat,l2)
print(result)
