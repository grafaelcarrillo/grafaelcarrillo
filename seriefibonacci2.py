def fibonacci(n):
    fibseries = [0, 1]
    for i in range (n-2):
        fibseries.append(fibseries[-1] + fibseries[-2])
    return fibseries
n=int(input("Introduzca el número de elementos de la serie de Fibonacci: "))
fibonaccinum = fibonacci(n)
print(f"Serie de Fibonacci hasta el término {n}: {fibonaccinum}")
