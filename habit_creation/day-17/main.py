"""
1. What is the benefit of putting your code into functions? -> To resuse the block of code.
2. Suppose you have: expense_pe.py  |  main.py, If read_data() is inside expense_pe.py, what do you think main.py needs to do to use it? Need to import the  expense_pe.py  into main.py to call the read_data() function.
3. What do you think this means? | "import csv" | What is Python actually doing when you write import csv? it import the csv module where we can use the methods written inside the library


Day 17:
Time: approx. 25min
Habit battle: not on 8pm but i complete the habit
What I built: modifie expense pipeline using import/module
What confused me: i achive how to import file if a py file inside a folder or in same folder with main.py but  i try but unable to achive how to import a file if a it is inside a nested folder 
What I learned: keep learing day by day to, create/update a project with structured way

"""

# import expense_pipeline as pe  # if in same as main.py
from src import expense_pipeline as pe  # inside a folder and folder is same with main.py

input_file = "habit_creation/day-17/expenses.csv"
get_csv_data = pe.read_data(input_file)
get_clean_data = pe.clean_data(get_csv_data)
get_process_data = pe.process_data(get_clean_data['clean_data'])

category_str = f"\nTotal rows: {(get_clean_data['valid_data_cnt'] + get_clean_data['invalid_data_cnt'])}  ||  Valid rows: {get_clean_data['valid_data_cnt']}  ||  Invalid rows: {get_clean_data['invalid_data_cnt']}\n\n"
total_amount = 0
for key, value in get_process_data.items():
    category_str += f"{key} → {value}\n"
    total_amount += value
category_str += f"\nTotal Expense → {total_amount}\n"
print(category_str)













