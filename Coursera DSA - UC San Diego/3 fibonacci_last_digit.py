"""
3. Last Digit of Fibonacci Number Problem
Compute the last digit of the n-th Fibonacci number.
    Input: An integer n.
    Output: The last digit of the n-th Fibonacci number.

Input format: An integer n.
Output format: The last digit of Fn.
Constraints: 0 ≤ n ≤ 106
Sample 1.
    Input: 3
    Output: 2
Sample 2.
    Input: 139
    Output: 1
    F139 = 50095301248058391139327916261.
"""


# Bad Solution - Convert to str and back to int
# def fibonacci_last_digit(n):
#     fibo_array = [0, 1]
#     for i in range(2, n + 1):
#         a = fibo_array[i - 1] + fibo_array[i - 2]
#         fibo_array.append(a)
#     last_digit = int(str(fibo_array[n])[-1])
#     return last_digit

def fibonacci_last_digit(n):
    fibo_array = [0, 1]
    for i in range(2, n + 1):
        a = fibo_array[i - 1] + fibo_array[i - 2]
        fibo_array.append(a)
    last_digit = fibo_array[n] % 10
    return last_digit


n = int(input())
print(fibonacci_last_digit(n))
