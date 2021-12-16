# Fibonacci  - Program to display the Fibonacci series for given number

n = int(input("How many number? "))

n1, n2 = 0, 1
count = 0


if n <= 0:
   print("Enter a positive integer")

elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1