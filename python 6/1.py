def tup(names_list):
    boys_count = 0
    girls_count = 0

    for name in names_list:
        if isinstance(name, tuple):
            boys_count += 1
        else:
            girls_count += 1

    return boys_count, girls_count

names = [("John",), "Alice", ("Mike",), "Emma", ("Tom",), "Sophia", ("Jack",), "Olivia"] 
boys, girls = tup(names)
print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")
