"""Employee records are stored in the form of a nested dictionary as follows:

Employee = {'emp1': {'name': 'Hameed', 'age': 29, 'Designation':'Programmer', 'Salary':50000},

    'emp2': {'name': 'Gurjeet','age': '45','Designation':'HR' 'Salary':30000 }

    'emp3': {'name': 'Madhav', 'age': '35' 'Designation':'Admin' 'Salary':40000}} 

Write a function that receives as input parameters a nested dictionary,
a designation d and a salary s (int), and updates the salaries to s for all the 
employees whose Designation is d.
"""
employee = {'emp1': {'name': 'Divyansh', 'age': 29, 'Designation':'Programmer', 'Salary':50}, 'emp2': {'name': 'Gurjeet','age': '45' , 'Designation':'HR', 'Salary' : 30000 }, 'emp3': {'name': 'Madhav', 'age': '35', 'Designation':'Admin', 'Salary':40000}} 

d = input('Enter the designation: ')
s = float(input('Enter the updated salary: '))
def upgrade(employee, d, s):

    
    for i in employee:
        if employee[i]['Designation'] == d:
            employee[i]["Salary"] = s

    return employee

print(upgrade(employee, d, s))
print(employee['emp1']['Designation'])

# a = []
# p = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# for i in range(len(p)):
#     a = a + [p[i][1]]

# a.sort()
# print(a[1])    
