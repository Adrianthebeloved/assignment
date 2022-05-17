# Assignment
# Create functions to calculate the following statistical measures:
# 1. Mean
# 2. Median
# 3. Variance
# 4. Standard Deviation
# 5. Skewness

# 1. Solution
# mean = sum of elements/ number of elements

# create an empty list
list = []
# How many elements are we working on?
n = int(input("Enter number of elements : "))
print(f'Enter the {n} numbers below')

# iterating till the range
for x in range(0, n):
    number = int(input(':> '))
    #append the number to the list
    list.append(number)
#now we define the mean function using sum() and len() functions
def avg(x):
    avg = sum(x)/len(x)
    #next we return the rounded up value 
    return round(avg,2)
#then we call the function with the given list argument
print('Solution 1')
print(f'# The mean is {avg(list)}')
print('')
print('Solution 2')

# 2. Solution
# median is the middle value in a list ordered from smallest to largest(vice versa). 

#now we define the median function
def median(x):
# now we rearrange the list from smallest to largest.
    list_2 = list.sort()
    if n%2 != 0:
        #If the number of values, n, is odd, 
        # then the median is the value in the (n+1)/2 position in the sorted list(or array) of values.
        median = int(((n+1)/2)-1)
        return list[median]
    else:
        # if the number of value is even, 
        # then the median is the sum of the 2 middle values.
        median1 = int((n/2)-1)
        median2 = int(n/2)
    
        return (list[median1] + list[median2])/2

print(f'# The median is {median(list)}')
print('')
print('Solution 3')

# 3. Solution Variance

def variance(x):
#we have earlier defined the avg variable so,
    variance = sum((i-avg(list))**2 for i in list)/(len(list)-1)
    # because variance is the (sum of the squares of (i-average))/n-1 
    # where i is each number in the iterable and n is the number of elements
    return round(variance,4)
print(f'# The variance is {variance(list)}')
print('')
print('Solution 4')

# 4. Solution: Standard Deviation

def std(x):
#standard deviation is the square root of variance so...
    std = (variance(list))**0.5
    return round(std,4)
print(f'# The standard deviation is {std(list)}')
print('')
print('Solution 5')

#5. Solution: Skewness
#skewness = 3(mean - median)/standard deviation

def skew():
    skew = 3*(avg(list) - median(list)) / std(list)
    return skew
print(f'# The Skewness is {skew()}')
print('')


