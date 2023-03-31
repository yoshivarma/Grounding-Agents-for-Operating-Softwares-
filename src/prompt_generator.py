from loader import get_data
from heuristics.random_heuristic import random_heuristic


QUESTION = "Please translate the instructions into actions:\n"
EXAMPLE_FORMAT = "Instruction: {input}\nActions: {actions}\n"
PROMPT_FORMAT = "Instruction:{input}\nActions: "

def format_prompt(prompt, example_count=0, heuristic='random'):
    res = QUESTION
    data = get_data()
    examples = get_data_from_heuristic(heuristic, data, example_count, prompt)
    for example in examples:
        res += EXAMPLE_FORMAT.format(input=example[0], actions=example[1])
    res += PROMPT_FORMAT.format(input=prompt)
    return res

def get_data_from_heuristic(heuristic, data, count, input_text):
    if heuristic == 'random':
        return random_heuristic(data, count, input_text)
    else:
        raise ValueError(f"Unknown heuristic: {heuristic}")


    
    

    
    
if __name__ == "__main__":
    res = format_prompt("create a new customer")
    print(res)