class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_bonus(self, bonus):
        self.salary = self.salary * bonus

    def describe(self):
        print(f"oo {self.name} makes {self.salary}")


def oo(employees):
    for _, employee in employees.items():
        happier_employee = Employee(employee["name"], employee["amount"])
        happier_employee.give_bonus(1.2)
        happier_employee.describe()


def fp(employees):
    happier_employee = apply(employees, 1.2, adjust)
    report_adjustment(happier_employee)


def apply(adjustees, adjust, adjustment):
    return [
        (adjustee["name"], adjustment(adjustee["amount"], adjust))
        for _, adjustee in adjustees.items()
    ]


def report_adjustment(adjusteds):
    for adjusted in adjusteds:
        print(f"fp {adjusted[0]} now {adjusted[1]}")


def adjust(value, by):
    return value * by


def main():
    employees_for_bonus = {
        1: {"name": "andy", "amount": 34000},
        2: {"name": "fred", "amount": 75000},
    }
    oo(employees_for_bonus)
    fp(employees_for_bonus)


if __name__ == "__main__":
    main()
