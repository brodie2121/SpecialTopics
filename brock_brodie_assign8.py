class Employee:

    emp_name = ''


Id_num = ''
emp_dept = ''
emp_job_title = ''

emp_obj1 = Employee()
emp_obj1.emp_name = 'Susan Meyers'
emp_obj1.Id_num = '47899'
emp_obj1.emp_dept = 'Accounting'
emp_obj1.emp_job_title = 'Vice President'

emp_obj2 = Employee()
emp_obj2.emp_name = 'Marke Jones'
emp_obj2.Id_num = '39119'
emp_obj2.emp_dept = 'IT'
emp_obj2.emp_job_title = 'programming'

emp_obj3 = Employee()
emp_obj3.emp_name = 'Joy Rogers'
emp_obj3.Id_num = '81774'
emp_obj3.emp_dept = 'Manufacturing'
emp_obj3.emp_job_title = 'Engineering'

print('Employee 1 details:')
print('Employee Name:', emp_obj1.emp_name)
print('Employee ID Number:', emp_obj1.Id_num)
print('Employee Department:', emp_obj1.emp_dept)
print('Employee Job Title:', emp_obj1.emp_job_title)
print()
print('Employee 2 details:')
print('Employee Name:', emp_obj2.emp_name)
print('Employee ID Number:', emp_obj2.Id_num)
print('Employee Department:', emp_obj2.emp_dept)
print('Employee Job Title:', emp_obj2.emp_job_title)
print()
print('Employee 3 details:')
print('Employee Name:', emp_obj3.emp_name)
print('Employee ID Number:', emp_obj3.Id_num)
print('Employee Department:', emp_obj3.emp_dept)
print('Employee Job Title:', emp_obj3.emp_job_title)
