num = int(input("Enter a number"))
prime = True

for i in range (2, int(num/2)+1):
    if num%i == 0:
        prime = False

if prime:
    print("prime")
else:
    print("not a prime")