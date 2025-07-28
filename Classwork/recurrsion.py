def numbers(n):
    if n==0:
        return 
    print(n)
    return numbers(n-1)
numbers(12)