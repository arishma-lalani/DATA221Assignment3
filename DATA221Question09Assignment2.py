# Question 9

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Request to access the url
wikipedia_machine_learning_url = "https://en.wikipedia.org/wiki/Machine_learning"

# This chunk of code is an extra measure to ensure that we aren't blocked from accessing the Wikipedia page
http_headers = {"User-Agent": "Mozilla/5.0"}
http_response = requests.get(wikipedia_machine_learning_url, headers=http_headers)

# # Parse the content from the web page using the BeautifulSoup package
parsed_html_content = BeautifulSoup(http_response.text, "html.parser")

# Find the main article content using the ID provided
main_content_div = parsed_html_content.find("div", id="mw-content-text")

# This function helps us to extract the text from the table row cells
def extract_cells_from_table_row(table_row):
    row_cell_texts = []
    for cell in table_row.find_all(["th", "td"], recursive=False):
        cell_text = " ".join(cell.get_text(" ", strip=True).split())
        row_cell_texts.append(cell_text)
    return row_cell_texts

# Find the first table that shows up with at least 3 rows
selected_table_element = None
all_table_rows_in_selected_table = None

# Go through all the tables in the main content part of the website
for table_element in main_content_div.find_all("table"):
    all_rows_in_table = table_element.find_all("tr")
    data_rows_in_table = []

    # Find the rows that contain actual data (<td> with non-empty text)
    for table_row in all_rows_in_table:
        if table_row.find("td") is not None:
            row_cells = extract_cells_from_table_row(table_row)
            if any(cell != "" for cell in row_cells):
                data_rows_in_table.append(table_row)

    # Select the first table with at least 3 rows
    if len(data_rows_in_table) >= 3:
        selected_table_element = table_element
        all_table_rows_in_selected_table = all_rows_in_table
        break

# Find headers and table data
table_header_cells = None  # Stores table header rows
table_data_matrix = []  # Stores table data rows

for table_row in selected_table_element.find_all("tr"):
    row_cell_texts = extract_cells_from_table_row(table_row)

    # Skip the rows that are empty
    if not any(cell != "" for cell in row_cell_texts):
        continue

    has_header_cells = table_row.find("th") is not None
    has_data_cells = table_row.find("td") is not None

    # If a row has only <th> and no <td>, treat it as the header
    if table_header_cells is None and has_header_cells and not has_data_cells:
        table_header_cells = row_cell_texts
    else:
        # Otherwise, treat it as a data row if it has <td> cells
        if has_data_cells:
            table_data_matrix.append(row_cell_texts)

# Determine the max number of columns in the data rows
max_columns_in_table = max((len(row) for row in table_data_matrix), default=0)

# If header exists but is shorter than the maximum number of columns, then pad it
if table_header_cells is not None:
    if len(table_header_cells) < max_columns_in_table:
        table_header_cells = table_header_cells + [
            f"col{i}" for i in range(len(table_header_cells) + 1, max_columns_in_table + 1)
        ]
    max_columns_in_table = max(max_columns_in_table, len(table_header_cells))
else:
    # If no header exists, then generate default column names like "Col1, col2,..."
    table_header_cells = [f"col{i}" for i in range(1, max_columns_in_table + 1)]

# Pad all data rows so that each row has the same number of columns as the header
padded_table_data = [
    row + [""] * (max_columns_in_table - len(row)) for row in table_data_matrix
]

# Save the table to "wiki_table.csv"
dataframe_table = pd.DataFrame(padded_table_data, columns=table_header_cells)
output_csv_file_path = "wiki_table.csv"
dataframe_table.to_csv(output_csv_file_path, index=False, encoding="utf-8")

# Print a message that confirms that the headings have been saved to the .txt file (only for user clarity)
print(f"Saved table to {output_csv_file_path}")
