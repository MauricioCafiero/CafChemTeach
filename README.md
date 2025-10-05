# CafChemTeach
A library and notebooks and such for the Module: *Python, Machine Learning and AI for Chemistry*

- [Intro to Python and Machine Learning](#introductory-python-and-machine-learning)
- [Intro to various LLM use cases](#intro-to-llms) 

## Introductory Python and Machine Learning

- See the [Python basics revision notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/PyCatchUp_CafChem.ipynb)
- See the [common Python techniques](https://github.com/MauricioCafiero/CafChem/blob/main/docs/python_basics.md)<br>
- See the [primer on regular expressions](https://github.com/MauricioCafiero/CafChem/blob/main/docs/regex.md) <br>
- See the [Python on RACC2 page](https://github.com/MauricioCafiero/CafChem/blob/main/docs/run_python_racc.md) <br>
- See the [sample notebook for PubChemPy usage](https://github.com/MauricioCafiero/CafChem/blob/main/notebooks/Pubchem_CafChem.ipynb).

### A Primer on SMILES
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/SMILES_primer_CafChem.ipynb) shows how SMILES strings are used to represent molecules

### Introduction to RDKit
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/RDKit_intro_CafChem.ipynb) shows how to use RDKit to explore molecules and molecular properties, including applications to medicinal chemistry. 

### Featurize molecules and train SciKit-learn models
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/Featurizing_SKLearn_CafChem.ipynb) shows how to featurize lists of SMILES strings using RDKit descriptors and how to then fit that data using models from SciKit-learn

### Featurize molecules and train a Multilayer perceptron using PyTorch
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/BasicMLP_CafChem.ipynb) shows how to featurize lists of SMILES strings using RDKit descriptors and how to then fit that data using a neural netowrk in PyTorch.

### Try temperature-based sampling on models from Huggingface
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/LLM_Sampling_CafChem.ipynb) shows how to download models and perform sampling

### Make a Gradio app
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/Gradio_CafChem.ipynb) demonstrates how to make a simple Gradio app.

## Intro to LLMs

- See the [Ollama for LLMs page](https://github.com/MauricioCafiero/CafChemTeach/blob/main/using_ollama.md) <br>
- See the [NotebookLM by Google page](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebookLM.md) <br>

### Demonstrate Transformer encoders and decoders
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/Transformers_demo_CafChem.ipynb) shows how decoders generate text autoregressively. Can be used with any model on Huggingface. Also shows how encoders fill in masked words.

### Simple AI Agent that can use tools
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/SimpleAgent_CafChem.ipynb) shows how to build an AI Agent that can use tools.

### Simple chatbot using the OpenAI GPT-OSS-20B open weights model
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/OpenAI_Chatbot_CafChem.ipynb). shows how to chat with OpenAI's open model. A second version of the notebook includes the reasoning trace in a separate textbox.

### Simple retrieval-augmented generation with the Gemma LLM
- A [sample notebook](https://github.com/MauricioCafiero/CafChemTeach/blob/main/notebooks/Simple_Rag_Chat_CafChem.ipynb) to upload a PDF and use Gemma to interact with the content of the document.
