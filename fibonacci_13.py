fib = [1,1]

len_fib = int(input("How many Fibonacci numbers do you want to generate? "))

def fibonacci_generator(len_fib):
    if len_fib == 1:
        return [1]
    else:
        while len_fib > len(fib):
            fib.append(fib[-1]+fib[-2])
        return fib

print(fibonacci_generator(len_fib))