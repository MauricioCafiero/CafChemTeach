# CafChemTeach
A library and notebooks and such for the Module: *Python, Machine Learning and AI for Chemistry*

- [Intro to various LLM use cases](#intro-to-llms) 
- [Intro to Python and Machine Learning](#introductory-python-and-machine-learning)

## Introductory Python and Machine Learning

- For some basic Python concepts, see the [common Python techniques](https://github.com/MauricioCafiero/CafChemTeach/blob/main/python_basics.md)<br>
- For searching strings, see the [primer on regular expressions](https://github.com/MauricioCafiero/CafChem/blob/main/regex.md) <br>
- To run Python libraries on the RACC2 system, see the [Python on RACC2 page](https://github.com/MauricioCafiero/CafChemTeach/blob/main/run_python_racc.md) <br>

### a Primer on SMILES
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/SMILES_primer_CafChem.ipynb) shows how SMILES strings are used to represent molecules

### Introduction to RDKit
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/RDKit_intro_CafChem.ipynb) shows how to use RDKit to explore molecules and molecular properties, including applications to medicinal chemistry. 

### Featurize molecules and train SciKit-learn models
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/Featurizing_SKLearn_CafChem.ipynb) shows how to featurize lists of SMILES strings using RDKit descriptors and how to then fit that data using models from SciKit-learn

### Featurize molecules and train a Multilayer perceptron using PyTorch
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/BasicMLP_CafChem.ipynb) shows how to featurize lists of SMILES strings using RDKit descriptors and how to then fit that data using a neural netowrk in PyTorch.


## Intro to LLMs

- For instructions on using Ollama for LLMs, see the [Ollama page](https://github.com/MauricioCafiero/CafChemTeach/blob/main/using_ollama.md) <br>
- For instructions on using Google's NotebookLM, see the [NotebookLM page](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebookLM.md) <br>

## Demonstrate Transformer encoders and decoders
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/Transformers_demo_CafChem.ipynb) shows how decoders generate text autoregressively. Can be used with any model on Huggingface. Also shows how encoders fill in masked words.

## Simple chatbot using the OpenAI GPT-OSS-20B open weights model
- [Chat with OpenAI's open model](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/OpenAI_Chatbot_CafChem.ipynb). A second version of the notebook includes the reasoning trace in a separate textbox.

## Simple retrieval-augmented generation with the Gemma LLM
- upload a PDF and [use Gemma to interact with the content of the document](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/Simple_Rag_Chat_CafChem.ipynb).
