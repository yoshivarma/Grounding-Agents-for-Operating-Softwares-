from model import run_model, get_flan, get_gpt2
from loader import get_data
from prompt_generator import get_prompt

model, tokenizer = get_flan("large")

# model, tokenizer = get_gpt2()

input_text = "create a new customer"

prompt = get_prompt(input_text,4)

output = run_model(model, tokenizer, prompt)

print(output)