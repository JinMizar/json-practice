#!/usr/bin/python3

import json

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    for repo in data[:5]:
        # Retrieve the fields
        name = repo['name']
        html_url = repo['html_url']
        updated_at = repo['updated_at']
        visibility = repo['visibility']
        
        # Create a comma-separated string format for the fields
        csv_line = f"{name},{html_url},{updated_at},{visibility}\n"
        
        csv_file.write(csv_line)
