import multiprocessing
import time


def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def calcular_fibonacci_paralelo(n, num_processos):
    pool = multiprocessing.Pool(processes=num_processos)
    sequencia = pool.map(fibonacci_recursivo, range(1, n + 1))

    pool.close()
    pool.join()

    return sequencia


def main():
    n = 40
    num_processos = multiprocessing.cpu_count()

    inicio = time.time()
    sequencia = calcular_fibonacci_paralelo(n, num_processos)
    final = time.time() - inicio

    print(sequencia)
    print(f'O método recursivo paralelo terminou em {final:.10f} segundos.\n')


if __name__ == '__main__':
    main()
