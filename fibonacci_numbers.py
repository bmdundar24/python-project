list = [1, 1]
i = 0
y = 0
while i <= 7:
    y = list[i] + list[i + 1]
    list.append(y)
    i += 1
print(list)
