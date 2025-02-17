def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def npr(n, r):
    return factorial(n) // factorial(n - r)

# Example usage
n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"nCr({n}, {r}) = {ncr(n, r)}")
print(f"nPr({n}, {r}) = {npr(n, r)}")