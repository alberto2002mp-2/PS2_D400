# Define the number we want the factors of
n = 362880

# Use a list comprehension to generate all pairs of factors
factor_pairs = [(i, n // i) for i in range(1, int(n**0.5) + 1) if n % i == 0]

# Display the result
print(factor_pairs)
