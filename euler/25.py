# F_1 = F_2 = 1

def fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':

    for index,x in enumerate(fib()):
        if len(str(x)) >= 1000:
            break

    print(f'answer = {index+1}')