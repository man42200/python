
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]

n=int(input("Enter a number between 0 and 19: "))

if 0 <= n < 20:
    print("number to code is",n, "-->",words[n])
else:
    print("Number out of range")
