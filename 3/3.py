def check_substring(str1, str2):
    if str1 in str2:
        return True
    elif str2 in str1:
        return True
    else:
        return False

string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
result = check_substring(string1, string2)
print(result) 