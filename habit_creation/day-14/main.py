"""
What is the difference between return and print()? return some value else NaN, print is function to print something in terminal
What does float("250.50") produce? 250.50 in float value
What happens if you execute float("abc")? valuerror
Why might if input_data['Amount'] not be enough to validate an amount? it gives error
What problem does try/except solve? if try block gives error then except block handles the exceptions


Day 14:
Time: 22min
Habit battle: didnot battle much
What I built: hanndling the exception in expense calculation
What confused me: to handle category '' as it not give error
What I learned: not fully but how to use try except

"""


def read_data(input_csv_file):
    #Open the CSV and get the data.
    import csv
    get_content = []
    with open(input_csv_file, "r") as csv_file:
        csv_read = csv.DictReader(csv_file)   
        for csv_data in csv_read:
            get_content.append(csv_data)
    return get_content

def clean_data(input_content):
    # remove unwanted spaces
    # normalize category names
    # convert amount from string → integer
    # handle invalid/missing data
    clean_data = []
    valid_data_cnt = 0
    invalid_data_cnt = 0
    for input_data in input_content:
        try:
            if input_data['Category']:
                input_data['Category'] = input_data['Category'].strip().title()
                input_data['Amount'] = float(input_data['Amount'].strip())
                clean_data.append(input_data)
                valid_data_cnt+=1
            else:
                invalid_data_cnt+=1
        except ValueError:
            invalid_data_cnt+=1
            print('Skip the invalid data')
    print(f"Valid rows: {valid_data_cnt}\nInvalid rows: {invalid_data_cnt}")
    return clean_data

def process_data(clean_content):
    #Calculate category totals.
    category_dict_amount = {}
    for clean_data in clean_content:
        category = clean_data['Category']
        amount = clean_data['Amount']
        if category not in category_dict_amount:
            category_dict_amount.update({category:amount})
        else:
            category_dict_amount[category] += amount

    category_str = '\n'
    for key, value in category_dict_amount.items():
        category_str += f"{key} → {value}\n"
    return category_str


input_file = "habit_creation/day-14/expenses.csv"
get_csv_data = read_data(input_file)
get_clean_data = clean_data(get_csv_data)
get_process_data = process_data(get_clean_data)
print(get_process_data)