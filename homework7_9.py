def is_prime(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        result = 'Простое' if isinstance(value, int) else 'Сложное'

        return f"{value} это {result}"

    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)


print(sum_three(2, 3, 6))