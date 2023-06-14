import time


def fibonacci_recursivo(n):
    """A abordagem recursiva para calcular a sequência de Fibonacci envolve a definição de um método que chama a si
    mesmo para obter os números desejados. Nesse caso, o método fibonacci_recursivo recebe um número n como entrada
    e retorna todos os números, até o n-ésimo número da sequência.

    Args:
        n (int): Quantidade iterações do método.

    Returns:
        list: Lista de números inteiros somados cumulativamente, de acordo com o método de Fibonacci.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def main():
    n = 40

    # Uso fibonacci recursivo:
    inicio = time.time()
    sequencia = [fibonacci_recursivo(i) for i in range(1, n + 1)]
    final = time.time() - inicio
    print(sequencia)
    print(f'O método recursivo terminou em {final:.10f} segundos.\n')


if __name__ == '__main__':
    main()
