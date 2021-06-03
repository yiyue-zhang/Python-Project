# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:58:07 2021

@author: Yi
"""

import numpy as np

revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#calculating profit for each month
profit = []
for i in range(0, 12):
    profit.append(round((revenue[i] - expenses[i]), -3))
print(profit)

#calculating profit after tac for each moth
profit_tax = []
for i in range(0, 12):
    profit_tax.append(profit[i] * .3)
print(profit_tax)

#calculating profit margin for each month
profit_margin = []
for i in range(0, 12):
    profit_margin.append(round(100 * (profit_tax[i] / revenue[i])))
print(profit_margin)

#calculating good months
mean_profit_tax = sum(profit_tax) / 12
good_month = []
for i in range(0, 12):
    if (profit_tax[i] > mean_profit_tax):
        good_month.append(i)
print(good_month)

#calculating bad months
bad_month = []
for i in range(0, 12):
    if (profit_tax[i] < mean_profit_tax):
        bad_month.append(i)
print(bad_month)

#calculating the best month
max_profit_tax = max(profit_tax)
best_month = []
for i in range(0, 12):
    if (profit_tax[i] == max_profit_tax):
        best_month.append(i)
print(best_month)

#calculating the worst month
min_profit_tax = min(profit_tax)
worst_month = []
for i in range(0, 12):
    if (profit_tax[i] == min_profit_tax):
        worst_month.append(i)
print(worst_month)

