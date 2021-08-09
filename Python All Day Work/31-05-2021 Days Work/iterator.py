lst = [1, 2, 3, 4, 5]

print(lst[0])
print(lst[1])

for item in lst:
    print(item)

lst = [1, 2, 3, 4, 5]

iter_obj = iter(lst)
print(iter_obj)

print(next(iter_obj))
print(next(iter_obj))

for item in iter_obj:
    print(item)

# print(next(iter_obj))
# print(iter_obj.__next__())

for i in iter_obj:
    print(i)


class SeriesNumber:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        number = self.num
        self.num += 1 # i++
        return number


series_number = SeriesNumber()

print(series_number.__next__())

for i in series_number:
    if i == 10:
        break
    print(i)