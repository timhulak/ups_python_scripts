'''
Keep accurate count of CPU


Total = total trailers pulled
CPU = hot + cold
Hot CPU = CPU - Cold CPU
Cold CPU = tally if cold 

	
'''

import numpy as np
import datetime as dt

#Variables
sort = 'Morning'
current_time = dt.datetime.now()
tim = "Tim Hulak"

#Lists
kills = [24,23,19,29,13]
other_kills = [13,6,5,6,2]
other_hot = [0,1,1,0,1]
other_cold = [9,2,2,5,0]
vegas_l = [1,0,0,0,0]
wahca_l = [0,0,0,0,0]
basin_l = [1,1,1,1,1]
recycle_l = [2,2,1,0,0]

#Calculations
vegas = sum(vegas_l)
wahca = sum(wahca_l)
basin = sum(basin_l)
recycle = sum(recycle_l)
hot_cpu_a = sum(kills) + sum(other_hot)
cold_cpu = sum(other_cold)
total = sum(kills) + sum(other_kills)
cpu = hot_cpu_a + cold_cpu
hot_cpu = cpu - cold_cpu

#output
print(f'{sort} Sort Daily Recap {current_time.strftime("%m-%d-%Y")}\n')
print(f'Total: {total}')
print(f'Planned: {cpu}')
print(f'\tOther Planned: {hot_cpu}')
print(f'\tUnplanned: {cold_cpu}')
print(f'Type 1: {basin}')
print(f'Type 2: {recycle}')
print(f'Type 3: {vegas}')
print(f'Type 4: {wahca}')
print(f"\n- {tim}")


