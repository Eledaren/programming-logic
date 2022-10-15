def fibonacci(a, b):
  for i in range(50):
    print(a)

    fib = a + b
    a = b
    b = fib

fibonacci(0, 1)