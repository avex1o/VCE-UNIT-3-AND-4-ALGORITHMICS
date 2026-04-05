def factorial(x): # Algorithm (factorial, input x)
    if x == 1: # Base case 1: if x is 1 then return 1
        return 1
    elif x == 0: # Base case 2: if x is 0 then return 1
        return 1 
    else: # return x times value from factorial of (x-1)
        return x * factorial(x-1)

num = factorial(3) # assign value of factorial to num
print(num) # print num 



def str_reversal(string):
    if not string:
        return ""
    return str_reversal(string[1:]) + string[0]

reverse = str_reversal("algorithmics")
print(reverse)





def fibonacci(num):
    if num == 0:
        return 1 # Base case 1: if x = 0 then return 1
    if num == 1:
        return 2 # Base case 2: if x = 1 then return 2
    else:
        return fibonacci(num - 1) * fibonacci(num - 2)  # return F(num - 1) times F(num - 2)

fib = fibonacci(5)
print (fib)





class perms: # the function for calculating permutations uses the recursive factorial function
    def factorial(x): # Algorithm (factorial, input x)
        if x == 1: # Base case 1: if x is 1 then return 1
            return 1
        elif x == 0: # Base case 2: if x is 0 then return 1
            return 1 
        else: # return x times value from factorial of (x-1)
            return x * factorial(x-1)
    
    def permutations(list, r): # input list and r, number of slots we want from the list to be arranged
        n = len(list) # n equals length of list
        return (factorial(n) / factorial(n-r)) # returns permutations using list and r via the factorial function

elements = [1,2,3,4,5,6,7,8,9]
permutations = perms.permutations(elements, 3)
print(permutations)