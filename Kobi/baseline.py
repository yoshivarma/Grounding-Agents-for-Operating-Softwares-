from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("test.log"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger()
    logger.info("<New run>")
    return logger


logger = setup_logger()


def get_model_tokenizer(model_name, max_length=512):
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.max_new_tokens = max_length
    return model, tokenizer

model_size = "large"

model, tokenizer = get_model_tokenizer(f"google/flan-t5-{model_size}")
logger.info("Model and tokenizer loaded")
text = "Tell a funny joke."
encoded = tokenizer.encode_plus(text, return_tensors="pt")
for _ in range(1):
    res = model.generate(**encoded)
    logger.info(f'Generated: {res.shape}')
    decoded = tokenizer.decode(res[0], skip_special_tokens=True)
    logger.info(f'Decoded: {decoded}')
