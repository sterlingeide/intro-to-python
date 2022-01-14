def value_pairs(obj1, obj2, key):
    arr = []
    arr.append(obj1.get(key))
    arr.append(obj2.get(key))
    return arr

object1 = {"name": 'One', "location": 'Remote', "age": 1}
object2 = {"name": 'Two', "location": 'San Francisco'}

print(value_pairs(object1, object2, 'location'))
print(value_pairs(object1, object2, 'name'))