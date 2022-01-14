#This is where we will write the tripler function
def tripler(arr):
    result =[]

    for i in arr:
        result.append(i * 3)

    return result

print(tripler([1,2,3]))
print(tripler([4,1,7]))

