# -*- coding: utf-8 -*-

import random
import current_question
from importlib import reload


class QuestionsGenerator:
    def __init__(self, level):
        self.level = level
        self.generate_operation()
        self.operation_object = None

    def generate_operation(self):
        while True:
            obj = OperationsGenerator(self.level)
            if obj.execution:
                self.operation_object = obj
                self.make_question()
                break

    def make_question(self):
        print(self.operation_object.operation)
        print(self.operation_object.operation_in_code)
        print(self.operation_object.operation_result)


class OperationsGenerator:
    def __init__(self, level):
        self.path_current_operation = 'current_question.py'
        self.level = level
        self.exponents = ('2', '2', '3')
        self.prob_pot_sqrt = 0.8
        self.LIMITS = (-100, 100)

        self.operation = None
        self.operation_in_code = None
        self.operation_result = None

        self.execution = self.execute()

    def execute(self):
        try:
            if self.level == 0:
                self.somador()
            elif self.level == 1:
                self.multiplicador()
            elif self.level == 2:
                self.calculista()
            elif self.level == 3:
                self.professor()
            else:
                self.matematico()
            return self.validator()
        except ZeroDivisionError:
            return False

    def generator(self, numbers, operators, k=4, pot=False, sqrt=False):
        nrs = random.choices(numbers, k=k)
        ors = random.choices(operators, k=k-1)

        if sqrt:
            prob = random.random()
            if prob > 0.8:
                ir = random.choice(range(k))
                nrs[ir] = '√' + str(nrs[ir]**2)
        if pot:
            prob = random.random()
            if prob > 0.8:
                ir = random.choice(range(k))
                nrs[ir] = str(nrs[ir]) + '^' + random.choice(self.exponents)

        operation = [str(nrs.pop(0))]
        while len(ors):
            operation.append(ors.pop(0))
            operation.append(str(nrs.pop(0)))

        # Transformar a operação em um código para retornar o resultado
        self.operation = operation.copy()
        self.write_operation(operation)

        # Obter o resultado da operação
        reload(current_question)
        self.operation_result = current_question.returns_result()

    def validator(self):
        condition1 = self.operation_result >= self.LIMITS[0]
        condition2 = self.operation_result <= self.LIMITS[1]
        if self.operation_result % int(self.operation_result) == 0:
            self.operation_result = int(self.operation_result)
            condition3 = True
        else:
            condition3 = False

        join_conditions = condition1 and condition2 and condition3
        return join_conditions

    def write_operation(self, operation):
        for i, item in enumerate(operation):
            if '^' in item:
                operation[i] = item.replace('^', '**')
            if '√' in item:
                operation[i] = item.replace('√', 'sqrt(') + ')'

        operation = ' '.join(operation)
        with open(self.path_current_operation, 'w') as arq:
            arq.write('from math import sqrt\n\n')
            arq.write('def returns_result():\n')
            arq.write(f'\tx = {operation}\n')
            arq.write(f'\treturn x\n')

        self.operation_in_code = operation

    def somador(self):
        numbers = range(0, 21)
        operators = ('+', '-')
        self.generator(numbers, operators)

    def multiplicador(self):
        numbers = range(0, 10)
        operators = ('+', '-', '*')
        self.generator(numbers, operators)

    def calculista(self):
        numbers = range(0, 10)
        operators = ('+', '-', '*', '/')
        self.generator(numbers, operators)

    def professor(self):
        numbers = range(0, 10)
        operators = operators = ('+', '-', '*', '/')
        self.generator(numbers, operators, pot=True, sqrt=True)

    def matematico(self):
        numbers = range(0, 10)
        operators = operators = ('+', '-', '*', '/', '^', '√')
        self.generator(numbers, operators)

qg = QuestionsGenerator(3)
