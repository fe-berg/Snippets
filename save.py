#!/usr/bin/env python3

import json

# Define a function to create a node
def create_node(node, tags, title, description, url):
    # Strip spaces from each tag
    tags = [tag.strip() for tag in tags]
    return {
        "node": node,
        "tags": tags,
        "title": title,
        "description": description,
        "url": url
    }

# Function to get user input and create a new node
def get_user_input():
    node = input("Enter node: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    title = input("Enter title: ")
    description = input("Enter description: ")
    url = input("Enter URL: ")
    return create_node(node, tags, title, description, url)

# Load existing nodes from file if it exists
try:
    with open("nodes.json", "r") as file:
        nodes = json.load(file)
except FileNotFoundError:
    nodes = []

# Add a new node from user input
new_node = get_user_input()
nodes.append(new_node)

# Convert nodes to JSON format
nodes_json = json.dumps(nodes, indent=4)

# Save to a file
with open("nodes.json", "w") as file:
    file.write(nodes_json)

print("New node has been added and saved to nodes.json")
