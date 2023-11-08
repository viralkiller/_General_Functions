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
    def read_last_csv_rows(file_name, limit):
        with open(file_name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            return list(csv_reader)[-limit:]

    @staticmethod
    def match_last_csv_rows(file_name, match_col, find_val, return_col, limit):
        status = 'NO_MATCH'
        return_val = ''

        get_rows = CSVOps.read_last_csv_rows(file_name, limit)

        for row in get_rows:
            if row and len(row) > match_col and row[match_col] == find_val:
                status = 'MATCH'
                return_val = row[return_col] if len(row) > return_col else None
                break

        return status, return_val

# Example of how the class is used
if __name__ == '__main__':
    csv_ops = CSVOps()

    col_count = csv_ops.count_csv_cols('db/intent_to_sell.csv')
    print('\nColumn count:', col_count)

    # Further operations can be added below...
