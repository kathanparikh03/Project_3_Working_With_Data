# imports all modules or packages or libraries 
import csv
import requests
import json 
import matplotlib.pyplot as plt
import numpy as np

# creates a function get_data_from_file that accepts the filename and file format as arguments; creates the format if it is in the filename
def get_data_from_file(fn, format=""):
  ''' gets data from file format and return as python objects for further calculations '''
  # creates and passes the format as an argument if it is in the filename 
  if format == '':
    if 'csv' in fn: 
      format = 'csv'
    elif 'json' in fn: 
      format = 'json'

  # if csv, handles csv file
  obj = []
  if format == 'csv':
    f = open(fn)
    reader = csv.reader(f)
    for row in reader: 
      obj.append(row)
    f.close()

  # if json, handles json file
  elif format == 'json':
    f = open(fn)
    data = json.load(f)
    for row in data: 
      obj.append(row)
    f.close()

  # returns object as python object for further calculation with the data
  return obj

# creates a function get_data_from_internet and passes the url as an argument to gather data; format is json by default for internet files
def get_data_from_internet(url, format="json"):
  ''' gets data from internet format and return as python objects for further calculations '''
  # gets data from internet
  r = requests.get(url)
  # stores data to "data" variable
  data = r.json()
  # returns data as python object for further calculation with the data
  return data

# creates a function get_index_for_column_label that accepts header row and column label as arguments
def get_index_for_column_label(header_row, column_label):
  ''' gets and returns the index for column label in "tax_return_data_2018.csv" file '''
  # runs a for loop to return the index of column label
  for i in range(len(header_row)): 
    if column_label in header_row[i]: 
      return i 

# creates a function get_state_name that passes the object and state code as arguments
def get_state_name(state_names, state_code):
  ''' gets and returns the state name from "states_titlecase.json" when a state code is passed as an argument '''
  # runs a for loop to return the the state name when state code is passed as an argument
  for item in state_names: 
    for key in item: 
      if item[key] == state_code: 
        return item["name"]

# creates a function get_state_population that passes the object and state name as arguments
def get_state_population(state_populations, state_name):
  ''' gets and returns the state population from "https://raw.githubusercontent.com/heymrhayes/class_files/main/state_populations_2018.txt"
      when a state name is entered as an argument '''
  # runs a for loop to store the key without the '.' and its value in a list
  state_population_lis = []
  for item in state_populations: 
    for key in item: 
      state_population_lis.append([key[1:], item[key]])
    # runs a for loop again to return the state population
    for item in state_population_lis: 
      if state_name in item: 
        return item[1]

# Question 1 -- creates a function average_taxable_income_per_return_across_all_groups that returns the calculation for national level data
def average_taxable_income_per_return_across_all_groups_national():
  ''' calculates and returns the average taxable income per return for national level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")
  # sets n1 to 0
  n1 = 0
  # sets taxable income to 0
  taxable_income_amount = 0
  # adds data to their specific variable
  for data in returns_data[1:]:
    n1 += int(data[4])  
    taxable_income_amount += int(data[96])
  # finds the average 
  avg_taxable__inc_per_rtn = (taxable_income_amount/n1) * 1000
  # returns the output by rounding it
  return round(avg_taxable__inc_per_rtn)

# Question 2 -- creates a function average_taxable_income_per_return_for_each_agi_group that returns the calculation for national level data
def average_taxable_income_per_return_for_each_agi_group_national():
  ''' calculates and returns the average taxable income per return per agi group for national level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")

  # sets n1 and taxable income amount to 0 for each agi group 
  n1_1, n1_2, n1_3, n1_4, n1_5, n1_6 = 0, 0, 0, 0, 0, 0
  agi_1_taxable_income_amount, agi_2_taxable_income_amount, agi_3_taxable_income_amount = 0, 0, 0
  agi_4_taxable_income_amount, agi_5_taxable_income_amount, agi_6_taxable_income_amount = 0, 0, 0
  # adds data to their specific variable
  for data in returns_data[1:]: 
    if data[3] == '1':
      n1_1 += int(data[4])
      agi_1_taxable_income_amount += int(data[96])
    elif data[3] == '2':
      n1_2 += int(data[4])
      agi_2_taxable_income_amount += int(data[96])
    elif data[3] == '3':
      n1_3 += int(data[4])
      agi_3_taxable_income_amount += int(data[96])
    elif data[3] == '4':
      n1_4 += int(data[4])
      agi_4_taxable_income_amount += int(data[96])
    elif data[3] == '5':
      n1_5 += int(data[4])
      agi_5_taxable_income_amount += int(data[96])
    elif data[3] == '6':
      n1_6 += int(data[4])
      agi_6_taxable_income_amount += int(data[96])

  # finds the average
  avg_taxable__inc_per_rtn_agi_1 = (agi_1_taxable_income_amount/n1_1) * 1000
  avg_taxable__inc_per_rtn_agi_2 = (agi_2_taxable_income_amount/n1_2) * 1000
  avg_taxable__inc_per_rtn_agi_3 = (agi_3_taxable_income_amount/n1_3) * 1000
  avg_taxable__inc_per_rtn_agi_4 = (agi_4_taxable_income_amount/n1_4) * 1000
  avg_taxable__inc_per_rtn_agi_5 = (agi_5_taxable_income_amount/n1_5) * 1000
  avg_taxable__inc_per_rtn_agi_6 = (agi_6_taxable_income_amount/n1_6) * 1000

  # appends average by rounding it to the list 
  avg_taxable__inc_per_rtn_agi = []
  avg_taxable__inc_per_rtn_agi.append(('Group 1', round(avg_taxable__inc_per_rtn_agi_1)))
  avg_taxable__inc_per_rtn_agi.append(('Group 2', round(avg_taxable__inc_per_rtn_agi_2)))
  avg_taxable__inc_per_rtn_agi.append(('Group 3',round(avg_taxable__inc_per_rtn_agi_3)))
  avg_taxable__inc_per_rtn_agi.append(('Group 4', round(avg_taxable__inc_per_rtn_agi_4)))
  avg_taxable__inc_per_rtn_agi.append(('Group 5', round(avg_taxable__inc_per_rtn_agi_5)))
  avg_taxable__inc_per_rtn_agi.append(('Group 6', round(avg_taxable__inc_per_rtn_agi_6)))

  # returns the output
  return avg_taxable__inc_per_rtn_agi

# Question 3 -- creates a function average_taxable_income_per_resident_per_state that returns the calculation for national level data
def average_taxable_income_per_resident_per_state():
  ''' calculates and returns the average taxable income per state for national level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")

  # appends the states name to the list
  state_names_lis = []
  for data in returns_data[1:]:
    if data[1] not in state_names_lis:
      state_names_lis.append(data[1])

  # appends the state name and its taxable income to the list
  state_int = []
  for data in returns_data[1:]:
    for state in state_names_lis: 
      if state in data[1:]:
        state_int.append([state, int(data[96])])

  # appends the state name and the sum of the taxable income for each state
  sum = 0
  sum_lis = []
  for name in state_names_lis: 
    for item in state_int: 
      if name in item[0]:
        sum += item[1]
        sum_lis.append([name, sum])

  # skips the elements 0-4 for each state and appends the last element to the list
  state_taxable_income_sum = []
  for i in range(5, len(sum_lis), 6):
    state_taxable_income_sum.append(sum_lis[i])

  # subtracts the data i+ 1 from i and appends it to the list
  state_taxable_income_final_sum = []
  state_taxable_income_final_sum.append(state_taxable_income_sum[0])
  for i in range(1, len(state_taxable_income_sum)):
    state_taxable_income_final_sum.append([state_taxable_income_sum[i][0], state_taxable_income_sum[i][1] - state_taxable_income_sum[i-1][1]])

  # gets data from internet and stores to "internet_file" variable
  internet_file = get_data_from_internet("https://raw.githubusercontent.com/heymrhayes/class_files/main/state_populations_2018.txt", format="json")

  # appends the population of each state to the list
  population_lis = []
  for data in internet_file: 
    for population in data.values(): 
      population_lis.append(population)

  # appends the average to the list
  final_avg_taxable_income_per_state = []
  for i in range(len(population_lis)):  
    final_avg_taxable_income_per_state.append((state_taxable_income_final_sum[i][1]/population_lis[i]) * 1000)

  # rounds each average
  final_avg = []
  for avg in final_avg_taxable_income_per_state:
    final_avg.append(round(avg))

  # appends state name and its average
  state_name_with_avg = []
  for item in zip(state_names_lis, final_avg): 
    state_name_with_avg.append(item)

  # returns the output 
  return state_name_with_avg

# gets the input from user and stores it to "state_code" for state level questions
state_code = input("Type the state code (capital letters, no space within and after): ")

# Question 4 -- creates a function average_taxable_income_per_return_across_all_groups that returns the calculation for state level data
def average_taxable_income_per_return_across_all_groups(): 
  ''' calculates and returns the average taxable income per return across all groups for state level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")
  # sets n1 and taxable income amount to 0
  n1 = 0 
  taxable_income_amount = 0 
  # runs a loop that add the total n1 and taxable income amount to its variable
  for data in returns_data[1:]: 
    if data[1] == state_code: 
      n1 += int(data[4])  
      taxable_income_amount += int(data[96])
  # finds the average
  avg_taxable__inc_per_rtn = (taxable_income_amount/n1) * 1000
  # returns the output by rounding it
  return round(avg_taxable__inc_per_rtn)

# Question 5 -- creates a function average_taxable_income_per_return_for_each_agi_group that returns the calculation for state level data
def average_taxable_income_per_return_for_each_agi_group(): 
  ''' calculates and returns the average taxable income per return for each agi group for state level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")
 
  # assigns n1 and taxable income amount to its value for each agi group
  for data in returns_data[1:]:
    if data[1] == state_code:
      if data[3] == '1':
        n1_1 = int(data[4])
        agi_1_taxable_income_amount = int(data[96])
      elif data[3] == '2':
        n1_2 = int(data[4])
        agi_2_taxable_income_amount = int(data[96])
      elif data[3] == '3':
        n1_3 = int(data[4])
        agi_3_taxable_income_amount = int(data[96])
      elif data[3] == '4':
        n1_4 = int(data[4])
        agi_4_taxable_income_amount = int(data[96])
      elif data[3] == '5':
        n1_5 = int(data[4])
        agi_5_taxable_income_amount = int(data[96])
      elif data[3] == '6':
        n1_6 = int(data[4])
        agi_6_taxable_income_amount = int(data[96])

  # finds the average 
  avg_taxable__inc_per_rtn_agi_1 = (agi_1_taxable_income_amount/n1_1) * 1000
  avg_taxable__inc_per_rtn_agi_2 = (agi_2_taxable_income_amount/n1_2) * 1000
  avg_taxable__inc_per_rtn_agi_3 = (agi_3_taxable_income_amount/n1_3) * 1000
  avg_taxable__inc_per_rtn_agi_4 = (agi_4_taxable_income_amount/n1_4) * 1000
  avg_taxable__inc_per_rtn_agi_5 = (agi_5_taxable_income_amount/n1_5) * 1000
  avg_taxable__inc_per_rtn_agi_6 = (agi_6_taxable_income_amount/n1_6) * 1000

  # appends each average by rounding it and appending it to the list with the labels 
  avg_taxable__inc_per_rtn = []
  avg_taxable__inc_per_rtn.append(('Group 1', round(avg_taxable__inc_per_rtn_agi_1)))
  avg_taxable__inc_per_rtn.append(('Group 2', round(avg_taxable__inc_per_rtn_agi_2)))
  avg_taxable__inc_per_rtn.append(('Group 3', round(avg_taxable__inc_per_rtn_agi_3)))
  avg_taxable__inc_per_rtn.append(('Group 4', round(avg_taxable__inc_per_rtn_agi_4)))
  avg_taxable__inc_per_rtn.append(('Group 5', round(avg_taxable__inc_per_rtn_agi_5)))
  avg_taxable__inc_per_rtn.append(('Group 6', round(avg_taxable__inc_per_rtn_agi_6)))

  # returns the output
  return avg_taxable__inc_per_rtn

# Question 6 -- creates a function average_dependents_per_return_for_each_agi_group that returns the calculation for state level data
def average_dependents_per_return_for_each_agi_group(): 
  ''' calculates and returns the average dependents per return for each agi group for state level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")

  # assigns n1 and dependents of each agi group to its variable
  for data in returns_data[1:]:
    if data[1] == state_code: 
      if data[3] == '1':
        n1_1 = int(data[4])
        avg_dependents_1 = int(data[13])
      elif data[3] == '2':
        n1_2 = int(data[4])
        avg_dependents_2 = int(data[13])
      elif data[3] == '3':
        n1_3 = int(data[4])
        avg_dependents_3 = int(data[13])
      elif data[3] == '4':
        n1_4 = int(data[4])
        avg_dependents_4 = int(data[13])
      elif data[3] == '5':
        n1_5 = int(data[4])
        avg_dependents_5 = int(data[13])
      elif data[3] == '6':
        n1_6 = int(data[4])
        avg_dependents_6 = int(data[13])

  # finds the average
  avg_dependents_per_rtn_agi_1 = avg_dependents_1/n1_1
  avg_dependents_per_rtn_agi_2 = avg_dependents_2/n1_2
  avg_dependents_per_rtn_agi_3 = avg_dependents_3/n1_3
  avg_dependents_per_rtn_agi_4 = avg_dependents_4/n1_4
  avg_dependents_per_rtn_agi_5 = avg_dependents_5/n1_5
  avg_dependents_per_rtn_agi_6 = avg_dependents_6/n1_6

  # appends each averages by rounding it to the list with the labels for each agi group
  avg_dependents_per_rtn = []
  avg_dependents_per_rtn.append(('Group 1', round(avg_dependents_per_rtn_agi_1, 2)))
  avg_dependents_per_rtn.append(('Group 2', round(avg_dependents_per_rtn_agi_2, 2)))
  avg_dependents_per_rtn.append(('Group 3', round(avg_dependents_per_rtn_agi_3, 2)))
  avg_dependents_per_rtn.append(('Group 4', round(avg_dependents_per_rtn_agi_4, 2)))
  avg_dependents_per_rtn.append(('Group 5', round(avg_dependents_per_rtn_agi_5, 2)))
  avg_dependents_per_rtn.append(('Group 6', round(avg_dependents_per_rtn_agi_6, 2)))

  return avg_dependents_per_rtn

# Question 7 -- creates a function percentage_return_with_no_taxable_inc_per_agi_group that returns the calculation for state level data
def  percentage_return_with_no_taxable_inc_per_agi_group(): 
  ''' calculates and returns the percentage return with no taxable income per agi group for state level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")

  # assigns n1 and no taxable amount of each group to its variable
  for data in returns_data[1:]:
    if data[1] == state_code:
      if data[3] == '1':
        n1_1 = int(data[4])
        agi_1_no_taxable_income_amount = (int(data[4])-int(data[95]))
      elif data[3] == '2':
        n1_2 = int(data[4])
        agi_2_no_taxable_income_amount = (int(data[4])-int(data[95]))
      elif data[3] == '3':
        n1_3 = int(data[4])
        agi_3_no_taxable_income_amount = (int(data[4])-int(data[95]))
      elif data[3] == '4':
        n1_4 = int(data[4])
        agi_4_no_taxable_income_amount = (int(data[4])-int(data[95]))
      elif data[3] == '5':
        n1_5 = int(data[4])
        agi_5_no_taxable_income_amount = (int(data[4])-int(data[95]))
      elif data[3] == '6':
        n1_6 = int(data[4])
        agi_6_no_taxable_income_amount = (int(data[4])-int(data[95]))

  # finds the percentage for each agi group 
  percntge_no_taxable__inc_per_rtn_agi_1 = (agi_1_no_taxable_income_amount/n1_1) * 100
  percntge_no_taxable__inc_per_rtn_agi_2 = (agi_2_no_taxable_income_amount/n1_2) * 100
  percntge_no_taxable__inc_per_rtn_agi_3 = (agi_3_no_taxable_income_amount/n1_3) * 100
  percntge_no_taxable__inc_per_rtn_agi_4 = (agi_4_no_taxable_income_amount/n1_4) * 100
  percntge_no_taxable__inc_per_rtn_agi_5 = (agi_5_no_taxable_income_amount/n1_5) * 100
  percntge_no_taxable__inc_per_rtn_agi_6 = (agi_6_no_taxable_income_amount/n1_6) * 100

  # appends each percentage to the list by rounding it with the labels
  percntge_no_taxable__inc_per_rtn = []
  percntge_no_taxable__inc_per_rtn.append(('Group 1', round(percntge_no_taxable__inc_per_rtn_agi_1, 2)))
  percntge_no_taxable__inc_per_rtn.append(('Group 2', round(percntge_no_taxable__inc_per_rtn_agi_2, 2)))
  percntge_no_taxable__inc_per_rtn.append(('Group 3',round(percntge_no_taxable__inc_per_rtn_agi_3, 2)))
  percntge_no_taxable__inc_per_rtn.append(('Group 4',round(percntge_no_taxable__inc_per_rtn_agi_4, 2)))
  percntge_no_taxable__inc_per_rtn.append(('Group 5',round(percntge_no_taxable__inc_per_rtn_agi_5, 2)))
  percntge_no_taxable__inc_per_rtn.append(('Group 6',round(percntge_no_taxable__inc_per_rtn_agi_6, 2)))

  # returns the ouput 
  return percntge_no_taxable__inc_per_rtn

# Question 8 -- creates a function average_taxable_income_per_resident that returns the calculation for state level data
def average_taxable_income_per_resident(): 
  ''' calculates and returns the average taxable income per resident for state level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")

  # appends the states name to the list
  state_names_lis = []
  for data in returns_data[1:]:
    if data[1] not in state_names_lis:
      state_names_lis.append(data[1])

  # adds total taxable income amount
  taxable_income_amount = 0
  for data in returns_data[1:]: 
    if data[1] == state_code: 
      taxable_income_amount += int(data[96])

  # stores the data from internet to "internet_file" variable
  internet_file = get_data_from_internet("https://raw.githubusercontent.com/heymrhayes/class_files/main/state_populations_2018.txt", format="json")

  # appends the population to the list
  population_lis = []
  for data in internet_file: 
    for population in data.values(): 
      population_lis.append(population)

  # finds the index and stores the population of the state 
  state_name_indx = state_names_lis.index(state_code)
  population = population_lis[state_name_indx]

  # finds the average
  avg_taxable__inc_per_res = (taxable_income_amount/population) * 1000
  # returns the output by rounding it
  return round(avg_taxable__inc_per_res)

# Question 9 -- creates a function percentage_of_returns_for_each_agi_group that returns the calculation for state level data
def percentage_of_returns_for_each_agi_group(): 
  ''' calculates and returns the percentage of returns for each agi group for state level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")

  # assigns total n1 to 0
  total_n1 = 0
  # stores n1 of each agi group to its variable
  for data in returns_data[1:]:
    if data[1] == state_code: 
      total_n1 += int(data[4])
      if data[3] == '1':
        n1_1 = int(data[4])
      elif data[3] == '2':
        n1_2 = int(data[4])
      elif data[3] == '3':
        n1_3 = int(data[4])
      elif data[3] == '4':
        n1_4 = int(data[4])
      elif data[3] == '5':
        n1_5 = int(data[4])
      elif data[3] == '6':
        n1_6 = int(data[4])

  # finds the percentage for each agi group 
  percentage_per__rtn_agi_1 = (n1_1/total_n1) * 100
  percentage_per__rtn_agi_2 = (n1_2/total_n1) * 100
  percentage_per__rtn_agi_3 = (n1_3/total_n1) * 100
  percentage_per__rtn_agi_4 = (n1_4/total_n1) * 100
  percentage_per__rtn_agi_5 = (n1_5/total_n1) * 100
  percentage_per__rtn_agi_6 = (n1_6/total_n1) * 100

  # appends the percentage to the list by rounding it and assigning labels
  percentage_per__rtn = []
  percentage_per__rtn.append(('Group 1', round(percentage_per__rtn_agi_1, 2)))
  percentage_per__rtn.append(('Group 2', round(percentage_per__rtn_agi_2, 2)))
  percentage_per__rtn.append(('Group 3', round(percentage_per__rtn_agi_3, 2)))
  percentage_per__rtn.append(('Group 4', round(percentage_per__rtn_agi_4, 2)))
  percentage_per__rtn.append(('Group 5', round(percentage_per__rtn_agi_5, 2)))
  percentage_per__rtn.append(('Group 6', round(percentage_per__rtn_agi_6, 2)))

  # returns the output 
  return percentage_per__rtn

# Question 10 -- creates a function percentage_of_taxable_income_for_each_agi_group that returns the calculation for state level data
def percentage_of_taxable_income_for_each_agi_group():
  ''' calculates and returns the percentage of taxable income for each agi group for state level data '''
  # stores data from file to returns_data variable
  returns_data = get_data_from_file("tax_return_data_2018.csv")

  # sets total taxable income to 0
  total_taxable_income = 0
  # assings each taxable income to its agi group by creating variables
  for data in returns_data[1:]:
    if data[1] == state_code: 
      total_taxable_income += int(data[96])
      if data[3] == '1':
        taxable_inc_1 = int(data[96])
      elif data[3] == '2':
        taxable_inc_2 = int(data[96])
      elif data[3] == '3':
        taxable_inc_3 = int(data[96])
      elif data[3] == '4':
        taxable_inc_4 = int(data[96])
      elif data[3] == '5':
        taxable_inc_5 = int(data[96])
      elif data[3] == '6':
        taxable_inc_6 = int(data[96])

  # finds the percentage for each agi group 
  percentage_per__taxinc_agi_1 = (taxable_inc_1/total_taxable_income) * 100
  percentage_per__taxinc_agi_2 = (taxable_inc_2/total_taxable_income) * 100
  percentage_per__taxinc_agi_3 = (taxable_inc_3/total_taxable_income) * 100
  percentage_per__taxinc_agi_4 = (taxable_inc_4/total_taxable_income) * 100
  percentage_per__taxinc_agi_5 = (taxable_inc_5/total_taxable_income) * 100
  percentage_per__taxinc_agi_6 = (taxable_inc_6/total_taxable_income) * 100

  # appends each percentage by rounding it with labels to the list
  percentage_per__taxinc = []
  percentage_per__taxinc.append(('Group 1', round(percentage_per__taxinc_agi_1, 2)))
  percentage_per__taxinc.append(('Group 2', round(percentage_per__taxinc_agi_2, 2)))
  percentage_per__taxinc.append(('Group 3', round(percentage_per__taxinc_agi_3, 2)))
  percentage_per__taxinc.append(('Group 4', round(percentage_per__taxinc_agi_4, 2)))
  percentage_per__taxinc.append(('Group 5', round(percentage_per__taxinc_agi_5, 2)))
  percentage_per__taxinc.append(('Group 6', round(percentage_per__taxinc_agi_6, 2)))
  
  # returns the output
  return percentage_per__taxinc

# Pie chart for Question 9 -- creates a function percentage_of_returns_for_each_agi_group_pie_chart that creates the pie chart for question 9
def percentage_of_returns_for_each_agi_group_pie_chart(): 
  ''' creates a pie chart image of percentage of returns for each agi group (Question 9) -- state level data '''
  # gets the full state name
  state_name = get_state_name(get_data_from_file("states_titlecase.json"), state_code)
  # list of labels and sizes (values for x and y axis)
  labels = []
  sizes = []
  # appends lables and sizes from the function return to its variables
  data = percentage_of_returns_for_each_agi_group()
  for i in data: 
    labels.append(i[0])
    sizes.append(i[1])

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
          shadow=True, startangle=90)
  ax1.axis('equal')  
  plt.title(label="Percentage of Returns for each Agi Group for " + state_name, loc='center', fontsize='12', fontstyle='oblique')

  # saves the image 
  plt.savefig("pie1_" + state_code + ".png")

# Pie chart for Question 10 -- creates a function percentage_of_taxable_income_for_each_agi_group_pie_chart that the pie chart for question 10
def percentage_of_taxable_income_for_each_agi_group_pie_chart():
  ''' creates a pie chart image of percentage of taxable income for each agi group (Question 10) -- state level data '''
  # gets the full state name
  state_name = get_state_name(get_data_from_file("states_titlecase.json"), state_code)
  # list of labels and sizes (values for x and y axis)
  labels = []
  sizes =  []
  # appends lables and sizes from the function return to its variables
  data = percentage_of_taxable_income_for_each_agi_group()
  for i in data: 
    labels.append(i[0])
    sizes.append(i[1])

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
          shadow=True, startangle=90)
  ax1.axis('equal')  
  plt.title(label="Percentage of Taxable Income for each Agi Group for " + state_name, loc='center', fontsize='12', fontstyle='oblique')

  # saves the image
  plt.savefig("pie2_" + state_code + ".png")

# Bar chart for Question 3 -- creates a function average_taxable_income_per_state_bar_chart that creates a bar chart for question 3
def average_taxable_income_per_state_bar_chart(): 
  ''' creates a bar chart image of average taxable income per state (Question 3) -- national level data '''
  np.random.seed(3)
  # list of labels and sizes (values for x and y axis)
  x = []
  y = []
  # sorts the data in descending order
  data = average_taxable_income_per_resident_per_state()
  data.sort(key = lambda x: x[1], reverse=True)
  # appends the x and y from the function return to its list
  for i in data:
    x.append(i[0]) 
    y.append(i[1]) 

  # plot
  fig, ax = plt.subplots()
  ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
  plt.title(label="Average Taxable Income (Per Resident) Per State", loc='center', fontsize='12', fontstyle='oblique')
  
  # saves the image
  plt.savefig("bar1.png")
  
# creates a function answer_header that displays the header for each question when returned 
def answer_header(question_number, question_labels):
 ''' returns the header string for each answer'''
 header = "\n"*2
 header += "="*60 + "\n"
 header += "Question " + str(question_number) + "\n"
 header += question_labels[question_number] + "\n"
 header += "="*60 + "\n"
 return header
# labels for each question 
question_labels = [
   "",
   "average taxable income per return across all groups",
   "average taxable income per return for each agi group",
   "average taxable income (per resident) per state",
   "average taxable income per return across all groups",
   "average taxable income per return for each agi group",
   "average dependents per return for each agi group",
   "percentage of returns with no taxable income per agi group",
   "average taxable income per resident",
   "percentage of returns for each agi_group",
   "percentage of taxable income for each agi_group"
 ]

# creates a function main that calls function for each question and writes the answer to a new text file with the header of each question
# calls the function for pie charts and bar graph of question 9, 10 and 3
def main():
  ''' calls the functions created for each question (national and state level data) and writes it into a new text file
      calls the functions created for pie charts and bar graph of question 9, 10 and 3 '''
  # creates a new file
  f = open("answers" + state_code + ".txt", "w")

  # Question 1 -- header and answer
  f.write(answer_header(1, question_labels))
  f.write('$   ' + str(average_taxable_income_per_return_across_all_groups_national()))

  # Question 2 -- header and answer
  f.write(str(answer_header(2, question_labels)))
  question_2_answer = average_taxable_income_per_return_for_each_agi_group_national()
  for i in question_2_answer: 
    f.write(i[0] + ": ${0:>8}".format(str(i[1])) + '\n')

  # Question 3 -- header and answer
  f.write(answer_header(3, question_labels))
  question_3_answer = average_taxable_income_per_resident_per_state()
  for i in question_3_answer: 
    f.write(i[0] + ': $   ' + str(i[1]) + '\n')
  
  # writes a general header to notify that further answer are based on state level questions
  f.write("\n"*2)
  f.write(str("="*60 + "\n"))
  f.write("State level information for" + ' ' + get_state_name(get_data_from_file("states_titlecase.json"), state_code)+ '\n')
  f.write(str("="*60 + "\n"))

  # Question 4 -- header and answer
  f.write(answer_header(4, question_labels))
  f.write('$   ' + str(average_taxable_income_per_return_across_all_groups()))

  # Question 5 -- header and answer
  f.write(answer_header(5, question_labels))
  question_5_answer = average_taxable_income_per_return_for_each_agi_group()
  for i in question_5_answer: 
    f.write(i[0] + ": ${0:>8}".format(str(i[1])) + '\n')

  # Question 6 -- header and answer
  f.write(answer_header(6, question_labels))
  question_6_answer = average_dependents_per_return_for_each_agi_group()
  for i in question_6_answer: 
    f.write(i[0] + ':     ' + str(i[1]) + '\n')
  
  # Question 7 -- header and answer
  f.write(answer_header(7, question_labels))
  question_7_answer = percentage_return_with_no_taxable_inc_per_agi_group()
  for i in question_7_answer: 
    f.write(i[0] + ": {0:>8}".format(str(i[1])) + '%' + '\n')

  # Question 8 -- header and answer
  f.write(answer_header(8, question_labels))
  f.write('$   ' + str(average_taxable_income_per_resident()))

  # Question 9 -- header and answer
  f.write(answer_header(9, question_labels))
  question_9_answer = percentage_of_returns_for_each_agi_group()
  for i in question_9_answer: 
    f.write(i[0] + ": {0:>8}".format(str(i[1])) + '%' + '\n')

  # Question 10 -- header and answer
  f.write(answer_header(10, question_labels))
  question_10_answer = percentage_of_taxable_income_for_each_agi_group()
  for i in question_10_answer: 
    f.write(i[0] + ": {0:>8}".format(str(i[1])) + '%' + '\n')

  # closes the file
  f.close()         

  # calls function for pie_chart 1
  percentage_of_returns_for_each_agi_group_pie_chart()                  
  # calls function for pie_chart 2
  percentage_of_taxable_income_for_each_agi_group_pie_chart()          
  # calls function for bar_chart 1 
  average_taxable_income_per_state_bar_chart()     

main()