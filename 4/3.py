def count_alphabat_number():
    a = input("Enter a string/number: ")
    alphabets = 0
    digits = 0
    
    for char in a:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
    
    print(f"Number of alphabets: {alphabets}")
    print(f"Number of digits: {digits}")

count_alphabat_number()