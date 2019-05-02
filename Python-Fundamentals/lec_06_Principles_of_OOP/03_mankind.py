import re


class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name[0].isupper():
            raise Exception('Expected upper case letter! Argument: firstName')
        if len(first_name) <= 3:
            raise Exception('Expected length at least 4 symbols! Argument: firstName')
        else:
            self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        if not last_name[0].isupper():
            raise Exception('Expected upper case letter! Argument: lastName')
        if len(last_name) <= 2:
            raise Exception('Expected length at least 3 symbols! Argument: lastName')
        else:
            self.__last_name = last_name


class Student(Human):
    def __init__(self, first_name, last_name, faculty_number):
        Human.__init__(self, first_name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, faculty_number):
        is_allowed = bool(re.match("^[A-Za-z0-9]*$", faculty_number))

        if not (5 <= len(faculty_number) <= 10) or not is_allowed:
            raise Exception('Invalid faculty number!')
        else:
            self.__faculty_number = faculty_number

    def __str__(self):
        return f'First Name: {self.first_name}\n' \
            f'Last Name: {self.last_name}\n' \
            f'Faculty number: {self.faculty_number}'


class Worker(Human):
    def __init__(self, first_name, last_name, salary, working_hours):
        Human.__init__(self, first_name, last_name)
        self.salary = float(salary)
        self.working_hours = float(working_hours)

    def get_salary_per_hour(self):
        return self.salary / 5 / self.working_hours

    @property
    def salary(self):
        return self.__salary

    @property
    def working_hours(self):
        return self.__working_hours

    @salary.setter
    def salary(self, salary):
        if salary < 10:
            raise Exception('Expected value mismatch! Argument: weekSalary')
        else:
            self.__salary = salary

    @working_hours.setter
    def working_hours(self, working_hours):
        if working_hours < 1 or working_hours > 12:
            raise Exception('Expected value mismatch! Argument: workHoursPerDay')
        else:
            self.__working_hours = working_hours

    def __str__(self):
        return f'First Name: {self.first_name}\n' \
            f'Last Name: {self.last_name}\n' \
            f'Week Salary: {self.salary:.2f}\n' \
            f'Hours per day: {self.working_hours:.2f}\n' \
            f'Salary per hour: {self.get_salary_per_hour():.2f}'


# student
stu_first_name, stu_last_name, stu_faculty_number = input().split()

# worker
wor_first_name, wor_last_name, wor_salary, wor_working_hours = input().split()

try:
    ivan = Student(stu_first_name, stu_last_name, stu_faculty_number)
    pesho = Worker(wor_first_name, wor_last_name, wor_salary, wor_working_hours)
    print(ivan)
    print()
    print(pesho)
except Exception as exe:
    print(exe)
