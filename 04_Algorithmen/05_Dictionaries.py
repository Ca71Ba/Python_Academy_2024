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
# print(animal["partner"]["hasChildren"])
print(f"Animal {animal['partner']['name']} has kids: {animal['partner']['hasChildren']}")


print(animal)     
del animal["type"]
del animal["partner"]
print(animal)

students = {
    "Klaus" : 12345,
    "Anna" : 23456,
}

for key, value in students.items():
    print(f"Student {key} has the ID {value}")

for key in students.keys():
    print(f"Student {key} is registered")


# print(students["Anna"])

# ------------------ Übrung ------------------

employees = [
    {"name" : "Alice", "position" : "Manager", "salary" : 75000 },
    {"name" : "Bob", "position" : "Developer", "salary" : 60000 },
    {"name" : "Charlie", "position" : "Designer", "salary" : 55000 }
]

total_salary = 0

for emp in employees:
    print(f"Employee {emp['name']} is a {emp['position']} with a salary of {emp['salary']}")
    total_salary += emp['salary']

print(f"Total salary of all employees is: {total_salary}")