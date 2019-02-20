# Logistics Terminal Applications. 
#### With python installed, run the scripts in the terminal. 

## a_estimate_loads.py
### In order to track Packages Per Trailer, I wrote a Python app that asks the user for some input: 
- Planned Gross Volume for that day
- Current volume processed
- Number of loads processed 
### Once the user has input this information, the app returns the average packages-per-trailer and an estimate of how many loads are remaining.
### Ex.
#### What is the planned Gross Volume for today? (User Input ->) 76000
#### What is current total volume? (User Input ->) 12000
#### How many loads have been processed?  (User Input ->) 27

#### Average PPT is 444 
#### 144 Estimated Loads remaining 

## a_cpu_count_ups.py
### An app to help tally the total processed load types for the end of the day report. Using the 'dt.datetime.now()' function after 'import datetime as dt', the date will update automatically. 
### The app calculates:
- Current Date
- Total Pacakges processed
- Planend Packages processed
- Unplanned Packages Processed
- Types of Unplanned Packages processed
- Signature at the end 
### In order to change the values, one must edit the lists in the script manually. 

### Ex.

#### Morning Sort Daily Recap 02-19-2019

#### Total: 140
#### CPU: 129
#### 	Hot CPU: 111
#### 	Cold CPU: 18
#### Basin: 5
#### Recycle: 5
#### Vegas: 1
#### WAHCA: 0

#### - Tim Hulak
