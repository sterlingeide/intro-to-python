def adults(people):
    results = []

    for person in people:
        if person.get('age') > 17:
            results.append(person.get('name'))
    
    return results

ppl = [
  {"name": 'Khalid Robinson', "age": 22},
  {"name": 'Ariel Winter', "age": 20},
  {"name": 'Post Malone', "age": 25},
  {"name": 'Willow Smith', "age": 17}
]

print(adults(ppl))