#!/usr/bin/python

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

money = float(input("Где деньги, Лебовски?! -> "))
# print(money)

for cent in per_cent.values():
    deposit.append(money * cent/100)

print(deposit)
print("Максимальная сумма, которую вы можете заработать: %.2f" % max(deposit))
