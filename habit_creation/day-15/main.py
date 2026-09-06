"""
1. What is the difference between: return and print() ? return value to calling function and print() shows data
2. What does this function currently return? Is it returning:  A. dictionary   ||   B. string   ||   C. list
        def process_data(...):
            ...
            return category_str
Ans: it retuning string

3. Why might returning the dictionary be more useful than returning a formatted string? we can use the dict key to present th value with our own structural way

---------------------------------------------------

Day 15:
Time: 26min aprox.
Habit battle: yester was day-15 but i didnot do it as i want to chill but for a moment i thouht do do but regret too for some moment and it's natural i guess but i miss 3days (count yerseterday) 
What I built: i modifie the processdata function in the existing code
What confused me: not much
What I learned: what we should actuall return so later we can process it like dict instead string

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
        except ValueError:
            data_cnt['invalid_data_cnt']+=1
            print('Skip the invalid data')
    print(f"\n\nTotal rows: {(data_cnt['valid_data_cnt'] + data_cnt['invalid_data_cnt'])}  ||  Valid rows: {data_cnt['valid_data_cnt']}  ||  Invalid rows: {data_cnt['invalid_data_cnt']}\n\n")
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
    return category_dict_amount


input_file = "habit_creation/day-14/expenses.csv"
get_csv_data = read_data(input_file)
get_clean_data = clean_data(get_csv_data)
get_process_data = process_data(get_clean_data)

category_str = ''
if isinstance(get_process_data, dict):
    total_amount = 0
    for key, value in get_process_data.items():
        category_str += f"{key} → {value}\n"
        total_amount += int(value)
    category_str += f"\nTotal Expense → {total_amount}\n"
print(category_str)