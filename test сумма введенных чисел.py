def sum_digits(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result

n = int(input())
print(sum_digits(n))