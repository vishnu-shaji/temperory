num1=int(input("enter first no"))
num2=int(input("enter second no"))
for i in range(1,num1):
            if num1 % i==0 and num2 % i==0:
                gcd=i
print(gcd)