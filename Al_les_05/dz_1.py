'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа
должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
 предприятий, чья прибыль ниже среднего.
 Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из
 модуля collections
'''

from collections import namedtuple

firm = namedtuple('firm', ['name', 'profit_q1', 'profit_q2', 'profit_q3', 'profit_q4', 'profit_year'])
firms = []
n = int(input("Введити кол-во предприятий: "))
total_profit = 0
for i in range(1, n+1):
    name = input(f"Название {i}-ого предприятия: ")
    profit_q1 = int(input("Прибыль за 1 квартал: "))
    profit_q2 = int(input("Прибыль за 2 квартал: "))
    profit_q3 = int(input("Прибыль за 3 квартал: "))
    profit_q4 = int(input("Прибыль за 4 квартал: "))
    profit_year = profit_q1 + profit_q2 + profit_q3 + profit_q4
    total_profit += profit_year
    firms.append(firm(name=name, profit_q1=profit_q1, profit_q2=profit_q2, profit_q3=profit_q3, profit_q4=profit_q4, profit_year=profit_year))
average_profit = total_profit / n
print(f"Средняя прибыль {i} предприятий {round(average_profit, 2)}: ")
print(f"Предприятия с прибылью выше средней: ")
for firm in firms:
    if firm.profit_year >= average_profit:
        print(firm.name)
print(f"Предприятия с прибылью неже средней: ")
for firm in firms:
    if firm.profit_year < average_profit:
        print(firm.name)