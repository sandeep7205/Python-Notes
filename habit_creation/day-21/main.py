"""
1. What does this mean?
value = None

Is None:

an empty string?
zero?
a missing/absent value?

"""




# import os
# from dotenv import load_dotenv
# import src.expense_pipeline as pe

# load_dotenv()

# json_file_path = os.getenv("EXPENSE_JSON_FILE")
# json_output_file_path = os.getenv("EXPENSE_output_JSON_FILE")
# csv_file_path = os.getenv("EXPENSE_CSV_FILE")
# app_name = os.getenv("APP_NAME")


# clean_json_data = {
#     'developer': {},
#     'expenses': {},
# }

# get_json_data = pe.read_json(json_file_path)

# clean_json_data['developer']['name'] = get_json_data['developer']['name'].strip().title()
# clean_json_data['developer']['role'] = get_json_data['developer']['role'].strip().title()
# clean_json_data['developer']['experience'] = get_json_data['developer']['experience'].strip().title()


# get_clean_data = pe.clean_data(get_json_data['expenses'])

# get_process_data = pe.process_data(get_clean_data['clean_data'])
# clean_json_data['expenses'] = get_process_data

# pe.write_json(json_output_file_path, clean_json_data)

# get_json_data = pe.read_json(json_output_file_path)
# print(get_json_data)