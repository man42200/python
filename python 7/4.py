import names

generated_names = {names.get_first_name() for _ in range(200)}
print("Generated names:", generated_names)

start_with_a = {name for name in generated_names if name.startswith('A')}
start_with_b = {name for name in generated_names if name.startswith('B')}

print("Names starting with A:", start_with_a)
print("Names starting with B:", start_with_b)
