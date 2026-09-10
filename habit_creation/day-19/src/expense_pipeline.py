import json
import csv

def read_data(input_csv_file):
    #Open the CSV and get the data.
    get_content = []
    with open(input_csv_file, "r") as csv_file:
        csv_read = csv.DictReader(csv_file)   
        for csv_data in csv_read:
            get_content.append(csv_data)
    return get_content

def clean_data(input_content):
    return_dict = {
        "clean_data": [],
        "valid_data_cnt": 0,
        "invalid_data_cnt": 0
    }
    for input_data in input_content:
        # handle invalid/missing data
        try:
            if input_data['Category']:
                # remove unwanted spaces
                # normalize category names
                input_data['Category'] = input_data['Category'].strip().title()
                # convert amount from string → integer
                input_data['Amount'] = float(input_data['Amount'].strip())

                return_dict['clean_data'].append(input_data)
                
                return_dict['valid_data_cnt']+= 1
            else:
                return_dict['invalid_data_cnt']+= 1
        except ValueError:
            return_dict['invalid_data_cnt']+= 1
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

def read_json(json_file_path):
    # Read from json file
    with open(json_file_path, "r") as read_file:
        get_data = json.load(read_file)
    return get_data


def write_json(json_file_path, dict_data):
    # write dict data into from json file
    with open(json_file_path, "w") as write_file:
        json.dump(dict_data, write_file)