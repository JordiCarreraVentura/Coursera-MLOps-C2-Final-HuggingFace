import ast
import re

import gradio as gr

from mylib.calculator import add

def summ(arg1: int | float, arg2: int | float) -> float | int:
    return ast.literal_eval(arg1) + ast.literal_eval(arg2)


with gr.Blocks() as demo:
    arg1 = gr.Textbox(label="Summand")
    arg2 = gr.Textbox(label="Summand")
    output = gr.Textbox(label="Sum Box")
    greet_btn = gr.Button("Sum")
    # greet_btn.click(fn=summ, inputs=[arg1, arg2], outputs=output)
    greet_btn.click(fn=add, inputs=[arg1, arg2], outputs=output)

demo.launch()
