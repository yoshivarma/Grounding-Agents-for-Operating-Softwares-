from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GPT2LMHeadModel
from logger import logger


def get_model_tokenizer(model_name, model_class):
    model = model_class.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    logger.info(f"Model and tokenizer loaded: {model_name}")
    return model, tokenizer


def run_model(model, tokenizer, text, max_length=128):
    logger.info(f"Running model on text: {text}")
    encoded = tokenizer.encode_plus(text, return_tensors="pt")
    res = model.generate(**encoded, max_length=max_length)
    decoded = [tokenizer.decode(output, skip_special_tokens=True)
               for output in res]
    for i, d in enumerate(decoded):
        logger.info(f"Generated {i+1} : {text} : {d}")
    return decoded


def get_flan(size='base'):
    return get_model_tokenizer(f"google/flan-t5-{size}", AutoModelForSeq2SeqLM)


def get_gpt2():
    return get_model_tokenizer("gpt2", GPT2LMHeadModel)
