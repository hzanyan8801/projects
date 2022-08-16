"""def even_check(number):
    return number % 2 ==0

print(even_check(20))
print(even_check(21))

============

def check_even_list(num_list):
    for number in num_list:
        if number % 2 ==0:
            return True
        else:
            pass
print(check_even_list([1,3,5]))
print(check_even_list([2,4,6]))

======================

def check_even_list(num_list):
    #return all the even numbers in a list 

    # placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 ==0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

print(check_even_list([1,2,3,4,5]))
print(check_even_list([1,2,3]))

"""

work_hours = [('Abby',100), ('Billy', 300), ('Cassie', 500), ('Donny', 300), ('Eli', 1000)]

def employee_check(work_hours):
    current_max = 0
    employee_of_the_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass

    #return
    return(employee_of_the_month,current_max)

print(employee_check(work_hours))
