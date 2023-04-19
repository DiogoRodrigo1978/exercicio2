def fibonacci_sequence(n):
    """Retorna uma lista com os n primeiros números da sequência de Fibonacci."""
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def is_fibonacci_number(n):
    """Verifica se n pertence à sequência de Fibonacci."""
    if n == 0:
        return True
    sequence = fibonacci_sequence(n+1)
    if n in sequence:
        return True
    else:
        return False

# Solicita ao usuário um número
n = int(input("Digite um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci_number(n):
    print(f"{n} pertence à sequência de Fibonacci!")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")
