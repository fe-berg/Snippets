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