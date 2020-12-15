num = int(input("What number factorial would you like?"))
product = 1

for i in range(num, 1, -1):
    product = product * i

print(product)