def is_prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i+=1

    return True

print(is_prime(2))
print(is_prime(10))
print(is_prime(11))
print(is_prime(9))
print(is_prime(2017))