def generate_pythagorean_triplets(max_side_length):
    triplets = []
    for a in range(1, max_side_length + 1):
        for b in range(a, max_side_length + 1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= max_side_length:
                triplets.append((a, b, int(c)))
    return triplets

max_side_length = 30
triplets = generate_pythagorean_triplets(max_side_length)
for triplet in triplets:
    print(triplet)