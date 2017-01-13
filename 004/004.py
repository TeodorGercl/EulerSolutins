def is_palindrom(number):
    if str(number) == str(number) [::-1]:
        return True
    else:
        return False

foo = 0
for i in range(1,1000):
    for j in range(1,1000):
        if is_palindrom(i*j) and i*j>foo:
            foo = i*j
print(foo)


