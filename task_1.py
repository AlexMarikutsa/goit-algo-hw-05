
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def print_caching_fibonacci():
    fib = caching_fibonacci()(10)
    print(fib(10))
    print(fib(15))

if __name__ == '__main__':
    print_caching_fibonacci()