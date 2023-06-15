import multiprocessing
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
        # Caso base: n é 0 ou 1
        return n
    else:
        # Chamadas recursivas para calcular o n-ésimo termo
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def calcular_fibonacci_paralelo(n, num_processos):
    """
    Calcula a sequência de Fibonacci de forma paralela usando multiprocessamento.

    Args:
        n (int): Número de termos da sequência desejados.
        num_processos (int): Número de processos a serem utilizados.

    Returns:
        list: Lista contendo a sequência de Fibonacci calculada.
    """
    # Cria um pool de processos com o número de processos especificado
    pool = multiprocessing.Pool(processes=num_processos)

    # Mapeia a função fibonacci_recursivo para cada número no intervalo de 1 a n
    sequencia = pool.map(fibonacci_recursivo, range(1, n + 1))

    # Encerra o pool de processos e aguarda até que todos os processos terminem
    pool.close()
    pool.join()

    return sequencia


def main():
    # Define o número de termos da sequência de Fibonacci que desejamos calcular
    n = 40

    # Obtém o número de processadores disponíveis no sistema
    num_processos = multiprocessing.cpu_count()

    # Armazena o tempo atual antes de calcular a sequência
    inicio = time.time()

    # Calcula a sequência de Fibonacci de forma paralela
    sequencia = calcular_fibonacci_paralelo(n, num_processos)

    # Calcula o tempo de execução do método recursivo paralelo
    final = time.time() - inicio

    # Imprime a sequência de Fibonacci calculada
    print(sequencia)

    # Imprime o tempo de execução do método recursivo paralelo
    print(f'O método recursivo paralelo terminou em {final:.10f} segundos.\n')


if __name__ == '__main__':
    # Chama a função principal do programa
    main()
