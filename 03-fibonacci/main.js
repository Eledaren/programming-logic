const fibonacci = (a, b) => {
  for(let i = 0; i < 50; i++) {
    console.log(a)

    let fib = a + b
    a = b
    b = fib
  }
}

fibonacci(0, 1)