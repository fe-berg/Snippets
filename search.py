#!/usr/bin/env python3

import json
from prettytable import PrettyTable
import re

# Function to wrap text to a specified width, breaking at spaces, commas, or points
def wrap_text(text, width):
    words = re.split(r'(\s|,|\.)', text)
    wrapped_text = ''
    line_length = 0
    
    for word in words:
        if line_length + len(word) > width:
            wrapped_text += '\n'
            line_length = 0
        wrapped_text += word
        line_length += len(word)
    
    return wrapped_text

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
            table.add_row([wrap_text(node["title"], 32), wrap_text(node["description"], 32), node["node"]])
    
    # Print the table with matching results
    print(table)

# Example usage
keyword = input("Enter a keyword to search: ")
search_nodes(keyword)
