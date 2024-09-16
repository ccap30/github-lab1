import read_csv
import json_converter
import search
import json

# Example input:
# user = 16w
# user ~ 16
# user < 16
# user > 16
# Special case: "User <ID>" is the same as "user = <ID>"

def main():
    csv_file_path = 'data.csv'
    json_file_path = 'data.json'
    
    # Step 1: Read CSV
    csv_data = read_csv.read_csv("files/google_review_ratings.csv")
    
    # Step 2: Convert to JSON
    json_data = json_converter.convert_to_json(csv_data)
    
    # Step 3: Save JSON to file
    json_converter.save_json_to_file(json_data, json_file_path)
    
    # Print JSON data
    # print("JSON Data:\n", json_data)

    # Step 4: Search in JSON
    should_search = True
    description = """[Search Google Review Ratings]
Please use the format \"User <ID>\" or \"<key> <operator> <value>\" to search in the JSON file.
For example:
    - "user 6" returns all data about "User 6"
    - "dining table < 0.53" returns all users with dining table ratings under 0.53
    - "wardrobe ~ 0.9" returns all users with wardrobe ratings containing the text "0.9"
Enter "exit" to exit."""
    print(description)
    while True:
        search_string = input("  >  ")
        if search_string.lower() == "exit":
            break

        success, results = search.search_json(json.loads(json_data), search_string)
        # If failed, search again
        if success == False:
            print(results)
        else:
            # Print search results
            print("Search Results:\n", json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
