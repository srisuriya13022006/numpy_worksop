# find if the given number is a palindrome or not?
   num = int(input())
num_str = str(num)
rev = num_str[::-1]
if num_str == rev:
    print("it is a palindrome")
else:
    print("not a palindrome")
