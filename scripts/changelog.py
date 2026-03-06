import json
import difflib


def create_changelog(old_data, new_data):

    old_str = json.dumps(old_data, indent=2).splitlines()
    new_str = json.dumps(new_data, indent=2).splitlines()

    diff = difflib.unified_diff(old_str, new_str)

    return "\n".join(diff)