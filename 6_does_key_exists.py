def does_key_exist(obj, key):
    if obj.get(key):
        return True
    return False

obj1 = {"company": 'General Assembly', "course": 'Software Engineering Immersive'}
print(does_key_exist(obj1, 'company'))
print(does_key_exist(obj1, 'name'))