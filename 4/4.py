def prime_perfect_armstrong_palindrome():
    n = int(input("Enter a number: "))
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime number")
    else:
        print("Not a prime number")
    if n > 0:
        armstrong_sum = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            armstrong_sum += digit ** 3
            temp //= 10
        if n == armstrong_sum:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")
    else:
        print("Not an Armstrong number")
    if str(n) == str(n)[::-1]:
        print("Palindrone number")
    else:
        print("Not a Palindrone number")
prime_perfect_armstrong_palindrome()