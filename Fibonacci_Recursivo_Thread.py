import threading
import time


# Classe para calcular Fibonacci em uma thread separada
class FibonacciThread(threading.Thread):
    def __init__(self, n):
        """
        Inicializa uma nova instância de FibonacciThread.

        Args:
            n (int): Número do termo desejado na sequência.
        """
        threading.Thread.__init__(self)
        self.n = n
        self.result = None

    def run(self):
        """
        Método executado pela thread. Calcula o termo da sequência de Fibonacci.
        """
        self.result = fibonacci_recursivo(self.n)

    def get_result(self):
        """
        Obtém o resultado calculado pela thread.

        Returns:
            int: Resultado do cálculo.
        """
        return self.result


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


def fib_rec_thread(n):
    """
    Calcula a sequência de Fibonacci usando threads.

    Args:
        n (int): Número de termos da sequência desejados.

    Returns:
        list: Lista contendo a sequência de Fibonacci calculada.
    """
    if n <= 1:
        return n
    else:
        thread1 = FibonacciThread(n - 1)
        thread2 = FibonacciThread(n - 2)

        # Inicia as threads
        thread1.start()
        thread2.start()

        # Aguarda a conclusão das threads
        thread1.join()
        thread2.join()

        return thread1.get_result() + thread2.get_result()


def main():
    # Define o número de termos da sequência de Fibonacci que desejamos calcular
    n = 40

    # Uso fibonacci recursivo com threads:
    inicio = time.time()
    sequencia = [fib_rec_thread(i) for i in range(1, n + 1)]
    final = time.time() - inicio
    print(sequencia)
    print(f'O método recursivo com threads terminou em {final:.10f} segundos.\n')


if __name__ == '__main__':
    # Chama a função principal do programa
    main()
