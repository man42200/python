def convert(input_list):
    uppercase = {item.upper() for item in input_list}
    return uppercase

input_list = [input("Enter the string: ") for i in range(5)]
uppercase= convert(input_list)
print(uppercase)