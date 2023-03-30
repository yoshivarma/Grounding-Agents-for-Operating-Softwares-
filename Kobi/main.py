from model import run_model, get_flan, get_gpt2

# model, tokenizer = get_flan("base")

model, tokenizer = get_gpt2()

input_text = "Once upon a time a"

output = run_model(model, tokenizer, input_text)

# print(output)
