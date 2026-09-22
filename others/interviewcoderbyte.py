# Problem: CSV to Sorted JSON

# You are given a URL that, when queried with a GET request, 
# returns a plain-text response body containing CSV-formatted data. 
# Each line of the response represents one record with three comma-separated fields,
#  in this order:

# name,email,number

# There is no header row — every line is a data record.

# Task:
# Write a function that:

# Fetches the data from the given URL.
# Parses the CSV content into individual records.
# Sorts the records in ascending order based on the email field (second column).
# Returns the result as a JSON array of objects, 
# where each object has the keys "name", "email", and "number".

# input - 
# John Doe,john@example.com,12345
# Amy Lee,amy@example.com,54321
# Bob Smith,bob@example.com,67890

# output - [
#   {"name": "Amy Lee", "email": "amy@example.com", "number": "54321"},
#   {"name": "Bob Smith", "email": "bob@example.com", "number": "67890"},
#   {"name": "John Doe", "email": "john@example.com", "number": "12345"}
# ]

import requests
import json

resp = requests.get("https://gist.githubusercontent.com/parasahuja-debug/18d254bb405e6833ba0edec8ab454d29/raw/46a6666ac583dda3669006b4e39df0a052553d64/ata.csv")
lines = resp.text.strip().split('\n')

data = []
for line in lines:
    if not line:
        continue
    fields = line.split(",")
    name = fields[0]
    email = fields[1]
    number = fields[2]
    data.append({
        "name": name,
        "email": email,
        "number": number
    })

data.sort(key=lambda x: x["email"])

result = json.dumps(data, indent=2)
print(result)