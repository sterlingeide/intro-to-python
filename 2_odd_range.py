def odd_range(end):
    arr = []
    num = 1

    while num <= end:
        if not num % 2 == 0:
            arr.append(num)
        num +=1
    return arr

print(odd_range(13))
    