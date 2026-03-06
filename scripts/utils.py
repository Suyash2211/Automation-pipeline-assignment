import os
import json

# function to save JSON files
def save_json(data, path):

    # create folder if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # open file and write json
    with open(path, "w") as f:
        json.dump(data, f, indent=4)