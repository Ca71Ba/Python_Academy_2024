
employee_salary_data = {}
employee = {"name": "", "salary": 0}

counter = 0

while counter < 3:
    employee["name"] = input("Enter employee name: ")
    employee["salary"] = int(input("Enter employee salary: "))
    
    employee_salary_data[employee["name"]] = employee["salary"]
    
    counter = len(employee_salary_data)

print(employee_salary_data)




