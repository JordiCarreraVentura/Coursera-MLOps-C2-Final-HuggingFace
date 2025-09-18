import sys

import click

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


@click.command()
@click.option('--prompt', prompt="Enter a text to summarize", help='The text to summarize.')
def main(prompt):
    MODEL = "sshleifer/distilbart-cnn-12-6"

    #uncomment to download model
    model = pipeline(
       "summarization",
       model=MODEL,
       revision="a4f8f3e",
    )

    #load model and tokenizer from disk
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)
    tokenizer = AutoTokenizer.from_pretrained(MODEL)

    def predict(prompt):
        # Truncate to max length allowed by the model
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            max_length=1024,       # model limit
            truncation=True        # cut off extra tokens
        )
        outputs = model.generate(
            **inputs,
            max_length=200,        # control summary length
            min_length=30,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return decoded
    
    sys.stdout.write(predict(prompt))


if __name__ == '__main__':
    main()
