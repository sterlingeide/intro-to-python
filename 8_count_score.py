def count_score(people):
    results = {}
    for person in people:
        if results.get(person.get("name")):
            results[(person.get("name"))] += person.get("score")
            
        else:
            results[(person.get("name"))] = person.get("score")
    return results

ppl = [ 
    {"name": "Pete", "score": 10},
    {"name": "Mike", "score" : 10},
    {"name": "Pete", "score": -8},
    {"name": "Dexter", "score": 12}
]

peeps = [
  {"name": "Pete", "score": 2},
  {"name": "Dexter", "score": 2},
  {"name": "Mike", "score": 2},
  {"name": "Dexter", "score": 2},
  {"name": "Mike", "score": 2},
  {"name": "Pete", "score": 2},
  {"name": "Dexter", "score": 2}
]

print(count_score(ppl))
print(count_score(peeps))