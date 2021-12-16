# Fibonacci  - Program to display the Fibonacci series for given number

def fib2(n): # return Fibonacci series up to n
   result = []
   n1, n2 = 0, 1
   count = 0

   if n <= 0:
      print("Enter a positive integer")

   elif n == 1:
      print("Fibonacci sequence upto",n,":")
      result.append(n1)
   else:
      print("Fibonacci sequence:")
      while count < n:
         result.append(n1)
         nth = n1 + n2
         # update values
         n1 = n2
         n2 = nth
         count += 1
   return result
def main():
   n = int(input("How many number? "))
   print(fib2(n))

if __name__ == '__main__' : main()