def natural(number):
    if not isinstance(number, int) or number <= 0:
        raise TypeError


def is_prime(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        natural(value)
        x = 2
        while x < value:
            if value % x != 0:
                x += 1
            else:
                print('Сложное')
                return value
        print('Простое')
        return value

    return wrapper


try:
    @is_prime
    def sum_three(*numbers):
        return sum(numbers)


    print(sum_three(2, 3, 6))

except TypeError:
    print('Это не натуральное число')
