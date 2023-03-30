import json
from logger import logger

PATH_TO_JSON = '../json_dataset/data.json'

def get_data():
    logger.info(f"Loading data from {PATH_TO_JSON}")
    with open(PATH_TO_JSON, 'r') as f:
        data = json.load(f)
    logger.info(f"Loaded {len(data)} examples")
    data = clean_data(data)
    logger.info(f"Cleaned data to {len(data)} examples")
    return data

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


if __name__ == "__main__":
    data = get_data()
    print(len(data))