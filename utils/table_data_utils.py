import csv
from typing import Tuple


def get_flextable_data_as_single_tuple() -> Tuple:
    # the latest CSV file path
    CSV_FILE_PATH = "test_data/FlexTable_Test_data.csv"
    all_cell_values = []

    try:
        with open(CSV_FILE_PATH, mode='r', newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)

            # Skip the header row
            next(reader)

            for row in reader:
                # Stripping from each cell is crucial for clean data
                all_cell_values.extend([cell.strip() for cell in row])

        # Converting the single, long list of all cell values into a single tuple
        return tuple(all_cell_values)

    except FileNotFoundError:
        print(f"Error: CSV file not found at {CSV_FILE_PATH}")
        # Return an empty tuple on failure
        return tuple()


# The variable flextable_all_values now holds all data as a single tuple
flextable_all_values = get_flextable_data_as_single_tuple()

# Structure of flextable_all_values:
# ('Tahsin', '10', 'CSE', ...)