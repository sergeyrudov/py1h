a = [2, 1, 58, 3, 10, 59, 456, 19]
i = 0
min_num = a[i]
max = a[i]
while i < len(a):
    if a[i] < min_num:
        min_num = a[i]
    if a[i] > max:
        max = a[i]
    i = i + 1
print (min_num), max


