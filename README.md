
# Search Google Review Ratings

## Dependencies
Python3

## Usage
`python3 main.py`

When prompted, enter your search query: \<key\> \<operator\> \<value\>

Supported operators: ['<', '>', '<=', '>=', "=", "==", "~"]
- "=" and "==" are implemented the same, they check for equality
- "~" checks if ratings contain the same text as your \<value\>

## Files
`main.py` - Contains main function

`files/google_review_rating.csv` - Default dataset used in `main.py`

`json_converter.py` - Converts CSV files into JSON, creates data.json file

`read_csv.py` - Reads a CSV file

`search.py` - Search functionality for JSON data files
 