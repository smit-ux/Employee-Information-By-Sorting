# sorting using custom key
employees = [
    {'Name': 'Smit', 'age': 25, 'salary': 10000},
    {'Name': 'Tim', 'age': 30, 'salary': 80000},
    {'Name': 'Sarah', 'age': 18, 'salary': 10500},
    {'Name': 'Mike', 'age': 40, 'salary': 15000},
{'Name': 'Apex', 'age': 25, 'salary': 10600},
    {'Name': 'Xie', 'age': 30, 'salary': 8020},
    {'Name': 'Lamburt', 'age': 18, 'salary': 11000},
    {'Name': 'Megha', 'age': 40, 'salary': 1500},
{'Name': 'Musk', 'age': 25, 'salary': 10000},
    {'Name': 'Shady', 'age': 30, 'salary': 98000},
    {'Name': 'Mosh', 'age': 18, 'salary': 10500},
    {'Name': 'Mithali', 'age': 40, 'salary': 715000},
{'Name': ' Turing', 'age': 25, 'salary': 107000},
    {'Name': ' Lin', 'age': 30, 'salary': 8000},
    {'Name': ' Hopkins', 'age': 18, 'salary': 91000},
    {'Name': 'Nikhil', 'age': 40, 'salary': 815000},
{'Name': 'Alan', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon', 'age': 30, 'salary': 88000},
    {'Name': 'John', 'age': 18, 'salary': 10200},
    {'Name': 'Devanshu', 'age': 40, 'salary': 315000},

]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')