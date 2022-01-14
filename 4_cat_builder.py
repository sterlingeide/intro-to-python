def cat_builder(name, color, toys):
    newCat = {
        "name": [],
        "color": [],
        "toys": []
    }
    i = 0

    newCat.get('name').append(name)

    newCat.get('color').append(color)

    for i in toys:
        newCat.get('toys').append(i)
    
    return newCat

print(cat_builder('Garfield', 'golden', ['scratching-post', 'yarn']))
print(cat_builder('Whiskers', 'rainbow', ['poptarts']))

