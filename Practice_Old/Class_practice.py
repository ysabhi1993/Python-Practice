class Employee:
    
    raise_pay = 1.05
    
    def __init__(self, first_name, last_name, salary):
        self.first = first_name
        self.last = last_name
        self.email = first_name + '.' + last_name + '@company.com'
        self.salary = salary

    #regular methods
    def fullname(self):
        return self.first + ' ' + self.last

    #regular methods
    def inc_pay(self):
        return (self.salary * self.raise_pay)

    #used to change a class variable
    @classmethod
    def set_raise_pay(cls,inc):
        cls.raise_pay = inc

    #used to create instances of a class.
    @classmethod
    def from_string(cls, emp_str):
        first,last,salary = emp_str.split("-")
        return cls(first, last, salary)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

class Developer(Employee):
    raise_pay = 1.10

    def __init__(self, first_name, last_name, salary, prog_lang):
        #two methods to inherit attributes from superclass
        super().__init__(first_name, last_name, salary)         #useful when there is only one super class
        Employee.__init__(self, first_name, last_name, salary)   #useful when there are multiple super classes
        self.prog_lang = prog_lang

    @classmethod
    def dev_inc(self, inc):
        self.raise_pay = inc

    

class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employees = None):
        #two methods to inherit attributes from superclass
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())







            
