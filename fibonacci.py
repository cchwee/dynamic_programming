# normal recursive version
# Given a number n, print n-th Fibonacci Number. 

def fibonacci(n:int) -> int:

    '''
    Input:      n is a positive integer value. Any negative n value will be handled as an incorrect input.
    Output:     The ouput is an integer which is the nth Fibonacci number.
    Complexity: The function is of exponential time O(2^n), as a tree will be recursively created 
                each time n is called. The higher the n, the closer we get to a growth == golden ratio. 
    '''
    
    # base cases
    if n < 0:
        print("Incorrect input n")
    if n == 0:
        return 0
    elif n <= 2: 
        return 1
        
    else:
        return fibonacci(n-1) + fibonacci(n-2)

'''
# Driver code for recursive fibonacci
'''
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(10))



# dynamic prorgamming - top down approach
def topdown_fibo(n: int) -> int:
    
    '''
    Input:      n is a positive integer value. Any negative n value will be handled as an incorrect input.
    Output:     The ouput is an integer which is the nth Fibonacci number.
    Complexity: The function is of linear time O(n), as a memo is created and all fib will only be computed once.
    '''

    # handle base cases, O(1)
    if n < 0:
        print("Incorrect input n")
    if n == 0:
        return 0
    elif n <= 2: 
        return 1

    # n is larger than 2
    else:

        # create a memo table
        memo = [None] * n 

        # initialise base cases
        memo[0] = 0
        memo[1] = 1
        
        # check if that value has alrd been counted
        # memo hasnt been counted before
        if memo[n] is None:

            # save memo[n] value
            memo[n] = topdown_fibo(n-1) + topdown_fibo(n-2)
    
        # return nth Fibonacci number
        return memo[n]


'''
Drver code
'''
print(topdown_fibo(0))
print(fibonacci(1))
print(fibonacci(10))
