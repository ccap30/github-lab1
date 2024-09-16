import json

operators = ['<', '>', '<=', '>=', "=", "==", "~"]

def matches(item, operator, value):
    if operator == "~":
        return value in item
    
    item = float(item)
    value = float(value)
    if operator == '<':
        return item < value
    elif operator == '>':
        return item > value
    elif operator == '<=':
        return item <= value
    elif operator == '>=':
        return item >= value
    elif operator == '==' or operator == '=':
        return item == value
    return False

def search_json(json_data, search_string):
    search_terms = search_string.split(" ")

    if search_terms[0].lower() == "user":
        # Special case: Convert "User <ID>" to "User = <ID>"
        if len(search_terms) == 2:
            search_string = f"User = {search_terms[1]}"
            search_terms = search_string.split(" ")
        else:
            # Ensure proper capitalization for User searches
            search_terms[0] = "User"
            search_string = ' '.join(search_terms)

    # Ensure the search_string contains only one operator
    search_operators = list(filter(lambda x: x in search_terms, operators))
    if len(search_operators) != 1:
        return False, "Invalid operator: Please reformat your search with either \"User <ID>\" or \"<key> <operator> <value>\""
    
    # Key, operator, and value variables
    operator = search_operators[0]
    operands = search_string.split(operator)
    key = operands[0].strip()  # Key is before operator
    value = operands[1].lower().replace("user", "").strip()  # Value is after

    # Error if there is nothing on the left-hand side (key == '')
    # or if there is exactly one value on the right-hand side (value != 'x')
    if len(key) == 0:
        return False, "Invalid key: Please reformat your search with either \"User <ID>\" or \"<key> <operator> <value>\": "

     # Error if there is exactly one value on the right-hand side (value != 'x')
    try:
        float(value)
    except:
        return False, "Invalid value: Please reformat your search with either \"User <ID>\" or \"<key> <operator> <value>\": "

    # Only accept keys found in the JSON file
    if key not in json_data[0]:
        return False, f"JSON does not contain key: {key}"

    # If searching for a user, we have to strip the User ID off the JSON data
    if key == "User":
        print(f"Searching for entries with {key} {operator} User {value}...")
        return True, [entry for entry in json_data if matches(entry[key].split(" ")[1], operator, value)]    
    
    print(f"Searching for entries with {key} {operator} {value}...")
    return True, [entry for entry in json_data if matches(entry[key], operator, value)]
