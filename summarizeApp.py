from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import gradio as gr

MODEL = "sshleifer/distilbart-cnn-12-6"

#uncomment to download model
from transformers import pipeline
model = pipeline(
   "summarization",
   model=MODEL,
   revision="a4f8f3e",
)

#load model and tokenizer from disk
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)
tokenizer = AutoTokenizer.from_pretrained(MODEL)

def predict(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded

# create an interface for the model
with gr.Interface(predict, "textbox", "text") as interface:
    interface.launch()
