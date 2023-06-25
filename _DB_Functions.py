import csv
from collections import defaultdict
import time
import os
import os.path
import shutil

class DB_Functions():
    def __init__(self):
        pass

    def append_Database_Row(self, db_path, data_row):
        with open(db_path, 'a', newline='') as db_File:
            writer = csv.writer(db_File)
            writer.writerow(data_row)

    def delete_Rows_With_Matching_Column(self, filename, column_name, value_to_find):
        # Create backup of original file
        shutil.copy(filename, filename + '.backup')
        # List to hold updated rows
        updated_data = []
        # Flag for whether a match is found
        match_found = False
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check if the row matches the value to find
                if row[column_name] == value_to_find:
                    print(f"Found matching value in row: {row}")
                    match_found = True
                else:
                    # Only add rows to updated_data if they don't match the value to find
                    updated_data.append(row)
        # If a match was found, indicate that rows have been removed
        if match_found:
            print(f"Rows with value '{value_to_find}' in column '{column_name}' have been removed.")
        else:
            print(f"No rows with value '{value_to_find}' in column '{column_name}' were found.")
        # Overwrite the original CSV file with the updated data
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=updated_data[0].keys())
            writer.writeheader()
            for row in updated_data:
                writer.writerow(row)

    def return_Field_Value_From_Row(self, filename, column_name, input_value_to_find, col_to_return):
        match_found = 0
        counter = 0
        val_to_return = None
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[column_name] == input_value_to_find:
                    match_found = 1
                    val_to_return = row[col_to_return]
                    counter += 1
        return match_found, val_to_return, counter

    def overwrite_Field_Value(self, filename, column_name, input_value_to_find, col_to_overwrite, new_value):
        match_found = 0
        counter = 0
        # Create backup of original file
        shutil.copy(filename, filename + '.backup')
        # List to hold updated rows
        updated_data = []
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[column_name] == input_value_to_find:
                    row[col_to_overwrite] = new_value
                    match_found = 1
                    counter += 1
                updated_data.append(row)
        # Overwrite the original CSV file with the updated data
        if match_found:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=updated_data[0].keys())
                writer.writeheader()
                for row in updated_data:
                    writer.writerow(row)
        return match_found, counter


    def replace_Values_In_Column(self, filename, column_name, old_value, new_value):
        # Create backup of original file
        shutil.copy(filename, filename + '.backup')

        # List to hold updated rows
        updated_data = []

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check if the row contains the old value
                if row[column_name] == old_value:
                    print(f"Found matching value in row: {row}")
                    # Replace the old value with the new value
                    row[column_name] = new_value
                    print(f"Replaced with: {row}")
                updated_data.append(row)

        # Overwrite the original CSV file with the updated data
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=updated_data[0].keys())
            writer.writeheader()
            for row in updated_data:
                writer.writerow(row)

if __name__ == '__main__':
    d = DB_Functions()
    #---return_Field_Value_From_Row(self,filename,column_name,input_value_to_find,col_to_return):
    #get_grade = d.return_Field_Value_From_Row('static/csv/ukaf.csv','Item_Name','Item6','Grade_1')
    #print(get_grade)
    #---overwrite_Field_Value(self, filename, column_name, input_value_to_find, col_to_overwrite, new_value):
    #replace_grade = d.overwrite_Field_Value('static/csv/ukaf.csv','Item_Name','Item6','Grade_1','F')
    #---append_Database_Row(self, db_path, data_row):
    #append_row = d.append_Database_Row('static/csv/ukaf.csv',['012','Item11','2023-06-11','X','C','A','Note11'])
    #---delete_Rows_With_Matching_Column(self, filename, column_name, value_to_find):
    #delete_row = d.delete_Rows_With_Matching_Column('static/csv/ukaf.csv','UKAF_ID','002')
    #---replace_Values_In_Column(self, filename, column_name, old_value, new_value):
    replace_all_A_s = d.replace_Values_In_Column('static/csv/ukaf.csv','Grade_1', 'A', 'G')
