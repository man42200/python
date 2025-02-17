def remove_substring(main_string, sub_string):
    return main_string.replace(sub_string, '')
onestring = input("Enter a string: ")
removestring = input("Enter a substring to remove: ")
finalstring = remove_substring(onestring, removestring)
print(finalstring) 