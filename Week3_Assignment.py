#Assignment: Write a function that takes in an integer n 
# and returns true or false if the integer is a prime number.
# Program to check if a number is prime or not



# # To take input from the user

# num = int(input("Enter a number: "))

# # prime numbers are greater than 1
# if num > 1:
#    # check for factors
#    for x in range(2,num):
#        if num % x == 0:
#            print(f"False\n{num} is not a prime number")
#            break
#    else:
#        print(f"True\n{num} is a prime number")

# #if num <= 1 it is not a prime number  

# else:
#    print(num,"is not a prime number")



#Solution 2
    # num = int(input("Enter a number: "))
# Prime numbers: only divisible by 1 and itself and 1 is not a prime number
# so prime numbers > 1 and since we dont have a range of numbers to choose
#  from, we set the limits of the range to be between 2 and num
# so given a range of >1 to <num we iterate through till we see num&i ==0
# then we print False and break and end the loop, if not, that means the num is
# a prime number so we print True
#
# prime number is > 1

num = int(input("Enter a number: "))
def prime(num):
    if num > 1:
   # iterate through the range to check if it has any factor
        for x in range(2,num):
            if num % x == 0:
                print(f"False\n{num} is not a prime number")
                break
        else:
            print(f"True\n{num} is a prime number")
#if num <= 1 it is not a prime number  so
    else:
        print(num,"is not a prime number")
prime(num)

# h=1
# while h<=10:
#     print(h)
#     h+=1