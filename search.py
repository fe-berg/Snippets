#!/usr/bin/env python3

import json
from prettytable import PrettyTable

# Function to search nodes for a keyword
def search_nodes(keyword):
    # Load nodes from file
    with open("nodes.json", "r") as file:
        nodes = json.load(file)
    
    # Initialize a table for displaying results
    table = PrettyTable()
    table.field_names = ["Title", "Description", "Node"]
    
    # Search for the keyword in tags, title, description, and node fields
    for node in nodes:
        if (keyword in node["tags"] or 
            keyword in node["title"] or 
            keyword in node["description"] or 
            keyword in node["node"]):
            table.add_row([node["title"], node["description"], node["node"]])
    
    # Print the table with matching results
    print(table)

# Example usage
keyword = input("Enter a keyword to search: ")
search_nodes(keyword)