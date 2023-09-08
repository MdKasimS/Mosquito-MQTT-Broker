from prettytable import PrettyTable

# Sample data as a list of dictionaries
data = [
    {"Name": "John", "Age": 30, "City": "New York", "NickName":"Laddu"},
    {"Name": "Alice", "Age": 25, "City": "San Francisco", "NickName":"Laddu"},
    {"Name": "Bob", "Age": 28, "City": "Chicago", "NickName":"Laddu"},
]

# Create a PrettyTable object and specify column names
table = PrettyTable(["Name", "Age", "City", "NickName"])

# Add data to the table
for row in data:
    table.add_row([row["Name"], row["Age"], row["City"], row["NickName"]])

# Set the alignment of columns (optional)
table.align["Name"] = "l"  # Left align the "Name" column
table.align["Age"] = "c"   # Center align the "Age" column
table.align["City"] = "r"  # Right align the "City" column

# Print the table
print(table)
