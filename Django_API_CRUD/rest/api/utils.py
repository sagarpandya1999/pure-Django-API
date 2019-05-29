import json

def is_json(json_data):
    try:
        somename = json.loads(json_data)
        is_json = True
    except ValueError:
        is_json = False

    return is_json