import json
def is_json(data):
    try:
        p_dict = json.dumps(data)
        valid = True
    except ValueError:
        valid = False
    return valid
