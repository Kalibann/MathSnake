# -*- coding: utf-8 -*-

# Importações
import sys
import random
from subprocess import PIPE, run


class QuestionsGenerator:
    # Método construtor
    def __init__(self, level):
        self.level = level
        self.generate_operation()
        self.operation_object = None
        self.dict_alternatives = None

    # Método para gerar uma operação
    def generate_operation(self):
        # Randomiza questões até achar uma válida de acordo com o validador da classe OperationsGenerator
        while True:
            obj = OperationsGenerator(self.level)
            if obj.execution:
                self.operation_object = obj
                break
        self.make_question()

    # Método para construir uma questão
    def make_question(self):
        difference_factor = 0.1

        # Calcular uma diferença de valores para fazer mais duas alternativas
        difference = abs(int(difference_factor * self.operation_object.operation_result))
        difference = 1 if not difference else difference

        range_operators = tuple(range(0, 2))
        alternatives_operators = (random.choice(range_operators), random.choice(range_operators))
        range_difference = tuple(range(1, difference + 1))
        alternatives_difference = (random.choice(range_difference), random.choice(range_difference))

        # Soma a diferença se o operador randômico for 1, subtrai se for 0
        alternatives = [self.operation_object.operation_result]
        for plus, diff in zip(alternatives_operators, alternatives_difference):
            if plus:
                alternatives.append(self.operation_object.operation_result + diff)
            else:
                alternatives.append(self.operation_object.operation_result - diff)

        # Caso uma alternativa tenha valor igual a outra, somá-la até ficar diferente
        while alternatives[1] == alternatives[0] or alternatives[1] == alternatives[2]:
            alternatives[1] += 1

        # Criar um dicionário com as alternativas
        random.shuffle(alternatives)
        self.dict_alternatives = dict(zip(['A', 'B', 'C'], alternatives))

        # Prints para conferir resultado
        print(self.operation_object.operation)
        print(self.operation_object.operation_in_code)
        print(self.operation_object.operation_result)
        print(self.dict_alternatives.items())


class OperationsGenerator:
    # Método construtor
    def __init__(self, level):
        self.path_current_operation = 'current_question.py'
        self.level = level
        self.exponents = ('2', '3')
        self.prob_pot_sqrt = 0.8
        self.LIMITS = (-100, 100)

        self.operation = None
        self.operation_in_code = None
        self.operation_result = None
        self.func_operation = None

        self.execution = self.execute()

    # Método para executar o processo, escolhendo as configurações corretas através do level passado
    def execute(self):
        try:
            match self.level:
                case 0:
                    self.adder()
                case 1:
                    self.multiplier()
                case 2:
                    self.arithmetician()
                case 3:
                    self.teacher()
                case 4:
                    self.mathematician ()
            return self.validator()
        except ZeroDivisionError:
            return False

    # Método para gerar uma operação
    def generator(self, numbers, operators, k=4, pot=False, sqrt=False):
        # Randomiza números e operadores
        nrs = random.choices(numbers, k=k)
        ors = random.choices(operators, k=k - 1)

        # Opção caso queira operações com raiz quadrada
        if sqrt:
            prob = random.random()
            if prob > 0.8:
                ir = random.choice(range(k))
                nrs[ir] = '√' + str(nrs[ir] ** 2)

        # Opção caso queira operações com potenciação
        if pot:
            prob = random.random()
            if prob > 0.8:
                ir = random.choice(range(k))
                nrs[ir] = str(nrs[ir]) + '^' + random.choice(self.exponents)

        # Juntar elementos da operação
        operation = [str(nrs.pop(0))]
        while len(ors):
            operation.append(ors.pop(0))
            operation.append(str(nrs.pop(0)))

        # Transformar a operação em um código para retornar o resultado
        self.operation = operation.copy()
        self.write_operation(operation)

        # Obter o resultado da operação
        self.operation_result = run([sys.executable, "-c", self.func_operation], stdout=PIPE,
                                    universal_newlines=True)
        self.operation_result = float(self.operation_result.stdout)

    # Método que efetua a validação da operação gerada
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

    # Método para escrever uma função de retorno para o resultado da operação gerada
    def write_operation(self, operation):
        for i, item in enumerate(operation):
            if '^' in item:
                operation[i] = item.replace('^', '**')
            if '√' in item:
                operation[i] = item.replace('√', 'sqrt(') + ')'

        operation = ' '.join(operation)

        self.func_operation = "from math import sqrt\n\n" \
                              "def func():\n" \
                              "\ttry:\n" \
                              f"\t\tx = {operation}\n" \
                              f"\texcept:\n" \
                              "\t\tx = -99999\n" \
                              "\tprint(x)\n" \
                              "func()"

        self.operation_in_code = operation

    # Método para gerar operações para o level adder: 0
    def adder(self):
        numbers = range(0, 21)
        operators = ('+', '-')
        self.generator(numbers, operators)

    # Método para gerar operações para o level multiplier: 1
    def multiplier(self):
        numbers = range(0, 10)
        operators = ('+', '-', '*')
        self.generator(numbers, operators)

    # Método para gerar operações para o level arithmetician: 2
    def arithmetician(self):
        numbers = range(0, 10)
        operators = ('+', '-', '*', '/')
        self.generator(numbers, operators)

    # Método para gerar operações para o level teacher: 3
    def teacher(self):
        numbers = range(0, 10)
        operators = operators = ('+', '-', '*', '/')
        self.generator(numbers, operators, pot=True)

    # Método para gerar operações para o level mathematician : 4
    def mathematician(self):
        numbers = range(0, 10)
        operators = operators = ('+', '-', '*', '/')
        self.generator(numbers, operators, pot=True, sqrt=True)


qg = QuestionsGenerator(3)
