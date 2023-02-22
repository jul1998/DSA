def factorial_number(n):
    ans = 1
    for i in range(n,0,-1):
        ans *= i
    print(ans)

def factorial_number(n):
    if n ==1 :
        return n
    return factorial_number(n-1) * n

print(factorial_number(5))

def fibonacciIterative(n):
    first_number = 0
    second_number = 1

    if n == 1 or n == 2:
        return n


    for number in range(n):
        temp = second_number
        second_number = first_number + second_number
        first_number = temp
        print(first_number+second_number, end="\n")

fibonacciIterative(10)

def fibonacciIterativeRecursive(n):
     if n<2:
         return n

     return fibonacciIterativeRecursive(n-1) + fibonacciIterativeRecursive(n-2)

fibonacciIterativeRecursive(10)