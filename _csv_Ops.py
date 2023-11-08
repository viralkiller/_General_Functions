import csv

class CSVOps:
    
    def __init__(self):
        pass  # The constructor has no functionality for now

    @staticmethod
    def count_csv_cols(filename):
        with open(filename, 'r') as csvfile:
            first_line = csvfile.readline()
        return first_line.count(',') + 1

    @staticmethod
    def append_to_csv(file_name, row_data):
        with open(file_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row_data)

    @staticmethod
    def write_to_csv(file_name, row_data):
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row_data)

    @staticmethod
    def read_last_csv_rows(file_name, limit, ignore_empty=True):
        with open(file_name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            all_rows = list(csv_reader)
            if ignore_empty:
                # Filter out empty rows if the flag is True
                filtered_rows = [row for row in all_rows if any(field.strip() for field in row)]
            else:
                filtered_rows = all_rows
            # Return the last 'limit' number of rows based on the flag
            return filtered_rows[-limit:]

    @staticmethod
    def get_column_index(file_name, column_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader, None)
            if headers:
                try:
                    return headers.index(column_name)
                except ValueError:
                    return None
        return None

    @staticmethod
    def match_last_csv_rows(file_name, match_column_name, find_val, return_column_name, search_limit, return_limit):
        
        match_col_index = CSVOps.get_column_index(file_name, match_column_name)
        return_col_index = CSVOps.get_column_index(file_name, return_column_name)
        
        if match_col_index is None:
            return 'COL_IN_NOT_FOUND', []
        if return_col_index is None:
            return 'COL_OUT_NOT_FOUND', []
        
        status = 'VAL_NOT_FOUND'
        matching_rows = []  # List to store all matching rows
        
        get_rows = CSVOps.read_last_csv_rows(file_name, search_limit, ignore_empty=True)
        
        for row in get_rows:
            if len(matching_rows) >= return_limit:
                break  # Stop searching once we have enough matches
            if row and row[match_col_index] == find_val:
                if return_column_name == '*':
                    matching_rows.append(row)
                else:
                    matching_row_value = row[return_col_index] if len(row) > return_col_index else None
                    matching_rows.append(matching_row_value)
                
                status = 'VAL_FOUND'
        
        # Only return the number of rows specified by return_limit
        return status, matching_rows[:return_limit]






# Example of how the class is used
if __name__ == '__main__':

    #Date,Product_ID,Product_Name,Merchant_Email

    c = CSVOps()

    filepath = 'db/intent.csv'

    #col_count = c.count_csv_cols(filepath)
    #print('\nColumn count:', col_count)

    #append = c.append_to_csv(filepath,[000,123,'Test','jules313@gmail.com'])

    #print(c.read_last_csv_rows('db/intent.csv', 3, ignore_empty=True))
    # If you want to include empty rows in the results
    #print(c.read_last_csv_rows('db/intent.csv', 3, ignore_empty=False))

    #find match
    status,matches = c.match_last_csv_rows(filepath, 'Product_ID', '789', 'Merchant_Email', 999, 2)
    print(matches)


