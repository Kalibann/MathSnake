from constants import *
from random import randint as rint
import math


class Question:
    def __init__(self, lvl):
        self.equation = []
        self.text = []
        self.answer = 101
        # self.generate_question(lvl)

    def generate_question(self, lvl, n_operations=4):
        numbers = (0, 10)
        operators = None
        match lvl:
            case 0:
                numbers = (0, 21)
                operators = ['+', '-']
            case 1:
                operators = ['*', '+', '-']
            case 2:
                operators = ['*', '/', '+', '-']
            case 3:
                operators = ['**', '*', '/', '+', '-']
            case 4:
                operators = ['√', '**', '*', '/', '+', '-']

        possible_squares = [n for n in range(*numbers) if math.isqrt(n) ** 2 == n]

        for operation in range(n_operations):
            operator = operators[rint(0, len(operators) - 1)]
            if operator == '√':
                self.equation.append(['√', possible_squares[rint(0, len(possible_squares) - 1)]])
                operator = operators[rint(1, len(operators) - 1)]
            else:
                self.equation.append(rint(*numbers))

            if operation != n_operations - 1:
                self.equation.append(operator)

        while self.answer > 100 or self.answer < -100:
            try:
                self.validate(numbers)
                self.solve(operators)
            except:
                self.generate_question( lvl, n_operations=4)

    def validate(self, numbers):
        cont_pot = 0
        for n in range(1, len(self.equation), 2):
            if self.equation[n] == '**':
                cont_pot += 1
                if cont_pot > 1:
                    self.equation[n] = ['/', '*', '+', '-'][rint(0, 3)]

            if self.equation[n] == '/':
                while self.equation[n + 1] == 0:
                    self.equation[n + 1] = rint(*numbers)

                if isinstance(self.equation[n - 1], int) and isinstance(self.equation[n + 1], int):
                    while not isinstance(self.equation[n - 1] / self.equation[n + 1], int):
                        self.equation[n - 1] = rint(*numbers)
                        self.equation[n + 1] = rint(1, numbers[1])
                else:
                    self.equation[n] = ['*', '+', '-'][rint(0, 2)]


    def solve(self, operators):
        if operators[0] == '√':
            operators.pop(0)
            for n in range(0, len(self.equation), 2):
                if isinstance(self.equation[n], list):
                    self.equation[n] = math.isqrt(self.equation[n][1])
        for op in operators:
            while op in self.equation:
                i = self.equation.index(op)
                match op:
                    case '**':
                        self.equation[i] = self.equation[i - 1] ** self.equation[i + 1]
                    case '*':
                        self.equation[i] = self.equation[i - 1] * self.equation[i + 1]
                    case '/':
                        self.equation[i] = self.equation[i - 1] // self.equation[i + 1]
                    case '+':
                        self.equation[i] = self.equation[i - 1] + self.equation[i + 1]
                    case '-':
                        self.equation[i] = self.equation[i - 1] - self.equation[i + 1]
                self.equation.pop(i + 1)
                self.equation.pop(i - 1)
        self.answer = self.equation[0]

