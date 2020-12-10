class Worker:
    def __init__(self,  name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname, self.position

    def get_total_income(self):
        return float(self._income_wage) + float(self._income_bonus)


employee_1 = Position('Ivan', 'Ivanov', 'engineer', {"wage": 20000, "bonus": 2000})
print(employee_1.get_full_name())
print(employee_1.get_total_income())
