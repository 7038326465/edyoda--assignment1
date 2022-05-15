# The Fibonacci Sequence is the series of numbers :

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# Every next number is found by adding up the two numbers before it.

# Expected Output : 1 1 2 3 5 8 13 21 34
# plz check below program for given output





num=int(input('enter a number:'))
n1,n2=0, 1
sum=0
if num<=0:
    print('enter value greter than 0')
else:
      for num in range(0,num):
        print(sum, end="  ")
        n1=n2
        n2=sum
        sum= n1+n2