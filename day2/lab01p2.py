# P2. Circuit Resistance Calculation
res1 = float(input('Enter value of first resistance: '))
res2 = float(input('Enter value of first resistance: '))

series_res = res1+res2
print(f"Series resistance of {res1} and {res2} is {series_res:.2f}")
parallel_res = (res1*res2)/series_res
print(f"Parellel resistance of {res1} and {res2} is {parallel_res:.2f}")
