import time


def fibonacci_recursivo(n):
    """
    Função recursiva para calcular o n-ésimo termo da sequência de Fibonacci.

    Args:
        n (int): Número do termo desejado na sequência.

    Returns:
        int: O n-ésimo termo da sequência de Fibonacci.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def main():
    # Define o número de termos da sequência de Fibonacci que desejamos calcular
    n = 40

    # Uso fibonacci recursivo:
    inicio = time.time()
    sequencia = [fibonacci_recursivo(i) for i in range(1, n + 1)]
    final = time.time() - inicio
    print(sequencia)
    print(f'O método recursivo terminou em {final:.10f} segundos.\n')


if __name__ == '__main__':
    # Chama a função principal do programa
    main()
