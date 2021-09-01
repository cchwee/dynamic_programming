# simple for loop solution
def sum_of_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

# dynamic programming method
def sum_of_n_dp(n):
    memo = [0 for i in range(n+1)]
    for i in range(1,n+1):
        memo[i] = memo[i-1] + i
    return memo[n]


'''
Driver code
'''
print(sum_of_n(0))
print(sum_of_n_dp(0))
print(sum_of_n(1))
print(sum_of_n_dp(1))
print(sum_of_n(15))
print(sum_of_n_dp(15))