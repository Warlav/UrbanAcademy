def is_prime(func):
    def wrapper(*args):
        prime = True
        for i in range(2, func(*args) - 1):
            if func(*args) % i == 0:
                prime = False
                break
            else:
                prime = True
        if prime == True:
            print('Простое')
            return func(*args)
        else:
            print('Составное')
            return func(*args)

    return wrapper


@is_prime
def sum_three(*args):
    result = sum(args)
    return result


result = sum_three(2, 3, 6)
print(result)
