from datetime import date


# a data type to use for some examples in the Spark Streaming section
class Person:
    def __init__(self, unique_id, first_name, middle_name, last_name, birth_date, ssn, salary):
        self.unique_id = unique_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.ssn = ssn
        self.salary = salary

    def age(self):
        return (date.today() - self.birth_date).days / 365  # approximately

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return "Person(" + \
               ",".join([self.first_name, self.last_name, str(self.birth_date), self.ssn, str(self.salary)]) + \
               ")"
