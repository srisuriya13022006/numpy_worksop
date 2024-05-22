#write a program to find the sum of digits of a given number'
 sum=0
def sumofdigit(num):
    sum+=num%10
    num=num//10
    print(sum)
a=123
sumofdigits(a)


   
