import json


def generate_diff(file1_path, file2_path):
    with open(file1_path) as file1, open(file2_path) as file2:
        file1 = json.load(file1)
        file2 = json.load(file2)
    sorted_diff = create_formatted_dict(file1, file2)
    return json.dumps(sorted_diff, indent=2, separators=("", ": "))


def create_formatted_dict(dict1, dict2):
    sorted_keys = sorted(set(dict1) | set(dict2))
    formatted_dict = {}
    for key in sorted_keys:
        if key in dict1 and key in dict2 and key not in formatted_dict:
            if dict1[key] == dict2[key]:
                formatted_dict[f"  {key}"] = dict1[key]
            else:
                formatted_dict[f"- {key}"] = dict1[key]
                formatted_dict[f"+ {key}"] = dict2[key]
        elif key in dict1:
            formatted_dict[f"- {key}"] = dict1[key]
        else:
            formatted_dict[f"+ {key}"] = dict2[key]
    return formatted_dict