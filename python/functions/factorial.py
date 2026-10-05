def factorial(n) -> int: 
    ans = 1
    for x in range(1,n+1) : 
        ans = ans * x

    return ans
num = int(input("Enter a Number : "))
print(factorial(num))