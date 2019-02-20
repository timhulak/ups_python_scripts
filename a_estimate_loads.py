planned_volume = input("What is the planned Gross Volume for today? ")
current_volume = input("What is current total volume? ")
current_processed_loads = input("How many loads have been processed? ")
avg_ppt = int(current_volume) / int(current_processed_loads)
print(f'\nAverage PPT is {round(avg_ppt)} ')
remaining_volume = int(planned_volume) - int(current_volume)
estimated_loads_remaining = int(remaining_volume) / int(avg_ppt)
print(f'{int(estimated_loads_remaining) } Estimated Loads remaining ')

