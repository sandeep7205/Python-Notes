"""
1). Your process_data() now returns:
{"Food": 1200, "Travel": 550}
Why is this better than returning:
Food → 1200
Travel → 550

1-Ans).  with the dictionary we can represent the data any kind of way but in string return the posibility of representation has no way other then the return format 

2). What is the purpose of try/except? try block execute the written code if any exception happen except execute it's code block.

3). If this happens: amount = float("abc") which exception do you expect? ValueError

4). In your current clean_data() function, how many different jobs is the function doing? Looping, data validating, type converting, counting, error handling, information printing. 



Day 16:
Time: i saw the task and think,  while thinking i slept for some time then up and got the idea and followed it
Habit battle: bettled with in like day2/3 but not that much 
What I built: expense calculation's clean_data() which returns  clean rows + quality information
What confused me: not much
What I learned:  how to return a data for future use

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
    return_dict = {
        "clean_data": [],
        "str_info": ''
    }
    clean_data = []
    data_cnt = {
    "valid_data_cnt" : 0,
    "invalid_data_cnt" : 0
    }
    for input_data in input_content:
        try:
            if input_data['Category']:
                input_data['Category'] = input_data['Category'].strip().title()
                input_data['Amount'] = float(input_data['Amount'].strip())
                clean_data.append(input_data)
                data_cnt['valid_data_cnt']+=1
            else:
                data_cnt['invalid_data_cnt']+=1
                return_dict['str_info'] += '\n Skip the invalid Category data'
        except ValueError:
            data_cnt['invalid_data_cnt']+=1
            return_dict['str_info'] += '\n Skip the invalid ValueError data'
    return_dict['str_info'] += f"\n\nTotal rows: {(data_cnt['valid_data_cnt'] + data_cnt['invalid_data_cnt'])}  ||  Valid rows: {data_cnt['valid_data_cnt']}  ||  Invalid rows: {data_cnt['invalid_data_cnt']}\n\n"
    return_dict['clean_data'] = clean_data
    return return_dict

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
    return category_dict_amount


input_file = "habit_creation/day-16/expenses.csv"
get_csv_data = read_data(input_file)
get_clean_data = clean_data(get_csv_data)
print(get_clean_data['str_info'])
get_process_data = process_data(get_clean_data['clean_data'])

category_str = ''
if isinstance(get_process_data, dict):
    total_amount = 0
    for key, value in get_process_data.items():
        category_str += f"{key} → {value}\n"
        total_amount += value
    category_str += f"\nTotal Expense → {total_amount}\n"
print(category_str)