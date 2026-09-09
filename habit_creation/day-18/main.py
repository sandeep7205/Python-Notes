"""
1. What's the difference between: [import expense_pipeline] and: [from src import expense_pipeline] 
ans. we can direct import the if the shares the same part , else we can use alias from if the file is in nested folder like src

2. Why did we separate main.py and expense_pipeline.py?  
ans. in this we the code structure exists and we can resuse the module file some where else for reuseablity.

3. Look at this: input_file = "habit_creation/day-17/expenses.csv" 
Is this: A. Business logic  or  B. Configuration
ans. Configuration

4. Imagine your program needs:
    CSV file location
    database password
    API key
    database host
Would you want these values directly inside your Python code?
ans. As these are Configuration realted and security related stuffs , so i shall put in safe place where only i can see and use 


Day 18:
Time: 23 min aprox
Habit battle: i didnot start at 8pm but i finish day-18
What I built: real world config a project
What confused me: how to use find_dotenv
What I learned: how to separet he config data from logic for security and reliablity


"""

import src.expense_pipeline as pe  # inside a folder and folder is same with main.py
from dotenv import load_dotenv
import os


# load_dotenv() # Load variables from .env into environment if in same file
load_dotenv(dotenv_path="habit_creation/day-18/config/.env") # Load from a specific absolute system path

app_name = os.getenv("APP_NAME")
input_file = os.getenv("EXPENSE_FILE") # Access the variables

get_csv_data = pe.read_data(input_file)
get_clean_data = pe.clean_data(get_csv_data)
get_process_data = pe.process_data(get_clean_data['clean_data'])

category_str = f"\n{app_name}\n---------------\nTotal rows: {(get_clean_data['valid_data_cnt'] + get_clean_data['invalid_data_cnt'])}\nValid rows: {get_clean_data['valid_data_cnt']}\nInvalid rows: {get_clean_data['invalid_data_cnt']}\n\n"
total_amount = 0
for key, value in get_process_data.items():
    category_str += f"{key} → {value}\n"
    total_amount += value
category_str += f"\nTotal Expense → {total_amount}\n"
print(category_str)