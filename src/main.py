from model import run_model, get_flan, get_gpt2
from loader import get_data
from prompt_generator import format_prompt
from random import sample

model, tokenizer = get_flan("large")

# model, tokenizer = get_gpt2()

data = get_data()

prompts = sample(data, 3)

for prompt in prompts:
    prompt = format_prompt(prompt[0],4)
    output = run_model(model, tokenizer, prompt)
    print(output)