# Using Ollama to interact with LLMs

Ollama is an easy-to-use app that allows you to chat with almost any open-weights LLM. All models are run locally and all data is kept local on your computer.

- [Install](#install) <br>
- [Use](#use) <br>
- [Other commands](#other-commands) <br>
- [Models to use](#models-to-use) <br>

## Install:
Install on Windows, MAC or Linux from the [Ollama Github Page](https://github.com/ollama/ollama) <br>

## Use:
- While Ollama on Windows provided an app, for text-based interactions it is much more efficient to run from the command line on Powershell 
(launch Windows Powershell or Powershell86 from your start button). Likewise on MAC you can use the terminal.
- Once on the command line, start an LLM with the following command:
```
ollama run llama3.2:1b
```
If this is the first time you have used a particular LLM, it will download the model first. Then it will open a chat that looks like this:
```
>>>
```
You can type your queries here:
```
>>> who is the strongest autobot?
```
and the replies will show up underneath. <br>
Once you are done with the chat, you can close the chat window like this:
```
>>> /bye
```
The model will still be running. You can close the model with:
```
ollama stop llama3.2:1b
```
## Other commands
- List all currently running models:
```
ollama ps
```
You can then stop a model as described above. 
- List all models currently installed on your computer:
```
ollama list
```
## Models to use:
The format of a given model us usually the name+version number:how many parameters. For example: llama3.2:1b is the llama model (from Meta), version 3.2, the 1 billion parameter version.
- On a typical Windows or MAC laptop without a fancy GPU, you will likely want to use smaller models. usually 1-2b parameter models will use 1-2 GB of memory to run; a 3-4b model will use 4-5 GB to run, etc.
- Suggested models. The first three are small models that have good general knowledge, while the last two have have dodgy general knowledge but are very small if you have limited resources. The Phi models are from Microsoft, Gemma models from are Google, and smollm models are from HuggingFace.  
  * **llama3.2:1b**
  * **phi4-mini**
  * **phi3.5** 
  * **gemma3:1b**
  * **smollm** 
- See all available models at the [Ollama library](https://ollama.com/library)
