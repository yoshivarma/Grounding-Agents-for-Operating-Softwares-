import json
from logger import logger

PATH_TO_JSON = '../json_dataset/data.json'
_loaded = None

def get_data():
    global _loaded
    if _loaded is not None:
        return _loaded
    logger.info(f"Loading data from {PATH_TO_JSON}")
    with open(PATH_TO_JSON, 'r') as f:
        data = json.load(f)
    logger.info(f"Loaded {len(data)} examples")
    data = clean_data(data)
    logger.info(f"Cleaned data to {len(data)} examples")
    _loaded = data
    return _loaded

def clean_data(data):
    data = filter(lambda x: x['status'] != 'incomplete', data)
    data = filter(lambda x: not contains_meta(x), data)
    return list(data)
    

def contains_meta(entry):
    if 'meta' in entry:
        return True
    if 'steps' in entry:
        for step in entry['steps']:
            if contains_meta(step):
                return True
    if 'output' in entry:
        for output in entry['output']:
            if contains_meta(output):
                return True
    return False

def entry_to_str(entry):
    outputs = get_outputs(entry)
    res = ""
    for output in outputs:
        res += "{action}[{param}]\n".format(action=output['action'], param=', '.join(output['param']))
    return res
    
def get_outputs(entry):
    res = []
    if 'output' in entry:
        res += entry['output']
    if 'steps' in entry:
        for step in entry['steps']:
            res += get_outputs(step)
    return res


if __name__ == "__main__":
    data = get_data()
    print(len(data))