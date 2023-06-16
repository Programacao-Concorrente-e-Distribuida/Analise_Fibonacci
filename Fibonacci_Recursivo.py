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

    # Armazena o tempo atual antes de calcular a sequência
    inicio = time.time()

    # Calcula a sequência de Fibonacci
    sequencia = [fibonacci_recursivo(i) for i in range(1, n + 1)]

    # Calcula o tempo de execução do método recursivo paralelo
    final = time.time() - inicio

    # Imprime a sequência de Fibonacci calculada
    print(sequencia)

    # Imprime o tempo de execução do método recursivo
    print(f'O método recursivo terminou em {final:.10f} segundos.\n')


if __name__ == '__main__':
    # Chama a função principal do programa
    main()
