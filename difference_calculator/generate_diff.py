import json


def generate_diff(file1_path, file2_path):
    with open(file1_path) as file1, open(file2_path) as file2:
        file1 = json.load(file1)
        file2 = json.load(file2)
    formatted_diff = create_formatted_diff(file1, file2)
    print(formatted_diff)
    return json.dumps(formatted_diff, indent=2, separators=("", ": "))


def create_formatted_diff(file1, file2):
    sorted_keys = sorted(set(file1) | set(file2))
    formatted_dict = {}
    for key in sorted_keys:
        if key not in formatted_dict and key in file1 and key in file2:
            if file1[key] == file2[key]:
                formatted_dict[f"  {key}"] = file1[key]
            else:
                formatted_dict[f"- {key}"] = file1[key]
                formatted_dict[f"+ {key}"] = file2[key]
        elif key in file1:
            formatted_dict[f"- {key}"] = file1[key]
        else:
            formatted_dict[f"+ {key}"] = file2[key]
    return formatted_dict
