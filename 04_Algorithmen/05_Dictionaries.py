person = {"name" : "Horst", "height" : 1.75, "age" : 42}
   
print(f"Name: {person['name']} und Alter: {person['age']}") 

persons = [
{"name" : "Klaus", "height" : 1.85, "age" : 42},
{"name" : "Anna", "height" : 1.65, "age" : 36},
{"name" : "Peter", "height" : 1.80, "age" : 29}
]

for p in persons:
    print(f"Name: {p['name']} und Alter: {p['age']}")   

animal = {"name" : "Berta", "type" : "Lion"} 

animal["partner"] = {"name" : "Rudi", "type" : "Lion", "hasChildren" : True} 
print(animal["partner"]["hasChildren"])

          

