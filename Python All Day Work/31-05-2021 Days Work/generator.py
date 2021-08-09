def print_number():
    return 10
    value = 10
    print(value)

result = print_number()
print(result)

def print_series_number():
    yield 10
    yield 15
    yield 20


result2 = print_series_number()
print(result2)
print(next(result2))

for item in result2:
    print(item)

def series_numbers():
    num = 1

    while num <= 10:
        yield num
        num += 1

values = series_numbers()
for item in values:
    print(item)