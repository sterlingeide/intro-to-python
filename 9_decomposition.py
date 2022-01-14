def is_prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i+=1

    return True

def first_n_primes(n):
    result = []
    i = 2
    while len(result) < n:
        if is_prime(i):
            result.append(i)
        i+=1
    return result

def sum_of_primes(n):
    arr = first_n_primes(n)
    i = 0
    tot = 0

    while i < len(arr):
        tot += arr[i]
        i+=1    
    return tot

print(sum_of_primes(4))

