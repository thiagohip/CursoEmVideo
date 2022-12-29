s = 0
for i in range(0, 501):
    if((i % 3 == 0) & (i % 2 != 0)):
        s += i
print(s)
