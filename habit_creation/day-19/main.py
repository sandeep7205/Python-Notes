"""
1.What Python data structure are you using here? category_dict_amount = {} -> Dictionary
2. What does csv.DictReader do? it read the file each line as Dictionary
3. What's the difference between: return data (return the value to caller function) and: print(data) (shows the data in the screen)
4. Imagine you have:
    Food → 1200
    Travel → 550
    Shopping → 800
Why might we want to save this result to a file instead of only printing it? to get the data in future instead of again go though the calculation process again.


Day 19:
Time: no seen
Habit battle: started lately but finished
What I built: mix of csv and json
What confused me: now i am overwrting "w" the prevous data but i try "a" and i appen but without , which shows error in json, so to know how to append with existing json data 
What I learned: how to mix up the functions and add to one of it


"""
import os
from dotenv import load_dotenv
import src.expense_pipeline as pe

load_dotenv()

json_file_path = os.getenv("EXPENSE_JSON_FILE")
csv_file_path = os.getenv("EXPENSE_CSV_FILE")
app_name = os.getenv("APP_NAME")




get_json_data = pe.read_json(json_file_path)
print(get_json_data)

get_csv_data = pe.read_data(csv_file_path)
get_clean_data = pe.clean_data(get_csv_data)
get_process_data = pe.process_data(get_clean_data['clean_data'])

pe.write_json(json_file_path, get_process_data)

get_json_data = pe.read_json(json_file_path)
print(get_json_data)