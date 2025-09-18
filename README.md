[![CI](https://github.com/nogibjj/Coursera-MLOps-C2-Final-HuggingFace/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Coursera-MLOps-C2-Final-HuggingFace/actions/workflows/cicd.yml)
[![Codespaces Prebuilds](https://github.com/nogibjj/Coursera-MLOps-C2-Final-HuggingFace/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/nogibjj/Coursera-MLOps-C2-Final-HuggingFace/actions/workflows/codespaces/create_codespaces_prebuilds)


## Lab: Hugging Face and Gradio Web Applications

### Overview

In this lab, you will work with Hugging Face and Gradio web applications to modify a Hello World app, run a summarization app, explore customizing summarization applications, and build a command-line tool using the click framework.

### Goals

By the end of this lab, you will:

1. Understand the benefits of using web frameworks like Gradio for machine learning solutions.
2. Learn how to modify and work with Hugging Face and Gradio applications.
3. Gain experience in building command-line tools using the click framework.

### Tasks

#### A. Modify Hello World

1. Run the following Hugging Face and Gradio web application `helloApp` by using: `python helloApp.py`.

2. Change this application to be a calculator that adds two numbers using the calculator function in `mylib`, i.e., `from mylib.calculator import add`.

**Reflection Question:** Why does a web framework like Gradio help build machine learning solutions faster?

#### B. Run the Summarization App

1. Run the `summarizeApp.py` by using `python summarizeApp.py` and type in some of the text found in `text.txt`. Preview it by pasting the URL into the web preview tool.

**Reflection Question:** How does the prediction change when you type more or less of the document?

#### C. Customize Summarization Applications

1. Run `load_model.py` to see a full example of how to customize summarization applications.

#### D. Build a Command-Line Tool

1. Build a command-line tool that is similar in functionality to the Gradio app using the click framework.

#### Checklist

1. <del>Modify Hello World
   1. <del>Run the following Hugging Face and Gradio web application `helloApp` by using: `python helloApp.py`.
   2. <del>Change this application to be a calculator that adds two numbers using the calculator function in `mylib`, i.e., `from mylib.calculator import add`.
   
   		**Done --->** `sumApp.py`
   
   3. <del>Why does a web framework like Gradio help build machine learning solutions faster?
2. <del>Run the Summarization App</del>
	1. <del>Run the `summarizeApp.py` by using `python summarizeApp.py` and type in some of the text found in `text.txt`. Preview it by pasting the URL into the web preview tool.</del>

    	**^------ Modified file (didn't work as it was)**
    	
	2. <del>How does the prediction change when you type more or less of the document?
3. <del>Customize Summarization Applications</del>
   1. <del>Run `load_model.py` to see a full example of how to customize summarization applications.</del>
   
    	**^------ Modified file (didn't work as it was)**
    
4. <del>Build a Command-Line Tool
	1. <del>Build a command-line tool that is similar in functionality to the Gradio app using the click framework.
    
   **Done --->** 
   		```
	   python summarizeCli.py --prompt "`cat input.txt`"
	   ```

### References

