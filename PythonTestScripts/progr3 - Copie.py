def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n_terms = 10
fib_sequence = fibonacci(n_terms)

print(f"Suite de Fibonacci jusqu'au {n_terms}-ème terme : {fib_sequence}")