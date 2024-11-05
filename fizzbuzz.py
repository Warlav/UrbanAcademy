a = []
for j in range(1, 101):
    a.append(j)
for i in a:
    if a[i] % 3 == 0 and a[i] % 5 == 0:
        a[i] = 'FizzBuzz'
    elif a[i] % 5 == 0:
        a[i] = 'Buzz'
    elif a[i] % 3 == 0:
        a[i] = 'Fizz'
    i = i + 1
print(a)