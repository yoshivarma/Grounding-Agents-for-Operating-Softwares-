from loader import get_data, entry_to_str
from heuristics import random_heuristic


PREFIX = "Please Give a list of actions to take to {goal} on NetSuite."
EXAMPLE_PREFIX = "Here is an example: If the goal is {goal} then the actions are:\n {actions}"

def get_prompt(input_text, example_count=0, heuristic='random'):
    res = PREFIX.format(goal=input_text)
    if example_count > 0:
        data = get_data()
        examples = get_data_from_heuristic(heuristic, data, example_count, input_text)
        for example in examples:
            res += "\n\n"
            res += format_example(example)
    return res

def format_example(example):
    goal = example['title']
    actions = entry_to_str(example)
    return EXAMPLE_PREFIX.format(goal=goal, actions=actions)
    

def get_data_from_heuristic(heuristic, data, count, input_text):
    if heuristic == 'random':
        return random_heuristic(data, count, input_text)
    else:
        raise ValueError(f"Unknown heuristic: {heuristic}")


    
    

    
    
if __name__ == "__main__":
    res = get_prompt("create a new customer")
    print(res)