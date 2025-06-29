import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
import pandas as pd
import numpy as np
import random

def setup_decoder(model_name: str):
  '''
    Setup the decoder model. Pulls model and tokenizer from HuggingFace, sets up device.

      Args:
        model_name: model to pull from HuggingFace.
      Returns:
        tokenizer, model, device
  '''
  device = "cuda" if torch.cuda.is_available() else "cpu"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

  print(f"model setup complete: {model_name}")
  return tokenizer, model, device

def decoder_inference(model, tokenizer, device, input_txt: str, n_steps: int, 
                      TEMP = 0.0, use_ramp = False):
  '''
    Takes input_txt and performs autoregressive inference. Captures the chosen token and
    probability at each step.

      Args:
        model: model to pull from HuggingFace.
        tokenizer: tokenier associated with the model
        device: cpu or cuda
        input_txt: prompt to decoder
        n_steps: how many tokens to use
        TEMP: temperature for inference
        use_ramp: Boolean, use temperature ramp?
      Returns:
        iterations: a list containing the input at each step, the chosen token 
                    and probability
  '''
  input_ids = tokenizer(input_txt, return_tensors="pt")["input_ids"].to(device)
  
  iterations = []
  c_o = int(n_steps*0.10)
  
  which_ramp = -1.0 #increasing ramp

  with torch.no_grad():
      for c in range(n_steps):
          iteration = dict()

          iteration["Input"] = tokenizer.decode(input_ids[0])
          output = model(input_ids=input_ids)

          # Select logits of the first batch and the last token and apply softmax
          next_token_logits = output.logits[0, -1, :]
          next_token_probs = torch.softmax(next_token_logits, dim=-1)

          if use_ramp:
            T_int = TEMP*(1/(1+np.exp(which_ramp*(c-c_o))))
          else:
            T_int = TEMP;

          if T_int < 0.015:
            token_id = torch.argmax(next_token_probs,axis=-1)
          else:
            scaled_probs = next_token_probs**(1/T_int)
            scaled_probs = scaled_probs / scaled_probs.sum()

            token_id = np.random.choice(scaled_probs.shape[-1], p=scaled_probs.cpu().numpy())
            token_id = torch.tensor(token_id).cuda()
            token_prob = next_token_probs[token_id].cpu().numpy()
            token_choice = (f"{tokenizer.decode(token_id)} ({100 * token_prob:.2f}%)")

          iteration[f"Choice"] = token_choice

          # Append predicted next token to input
          input_ids = torch.cat([input_ids, token_id.unsqueeze(0).unsqueeze(0)], dim=-1)

          iterations.append(iteration)
  return iterations

def decoder_list_probs(model, tokenizer, device, input_txt: str, n_steps: int, 
                    TEMP = 0.0, number_to_return = 5, use_ramp = False):
  '''
    Takes input_txt and performs autoregressive inference. Captures the top
    number_to_retun tokens and their probabilities at each step. Autoregresion based
    on greedy decoding.

      Args:
        model: model to pull from HuggingFace.
        tokenizer: tokenier associated with the model
        device: cpu or cuda
        input_txt: prompt to decoder
        n_steps: how many tokens to use
        TEMP: temperature for inference
        number_to_return: how many tokens to return per step
        use_ramp: Boolean, use temperature ramp?
      Returns:
        iterations: a list containing a dictionary for each step conatins the input at each step, 
                    the top number_to_return tokens and their probabilities.
  '''
  input_ids = tokenizer(input_txt, return_tensors="pt")["input_ids"].to(device)
  
  iterations = []
  c_o = int(n_steps*0.10)
  
  which_ramp = -1.0 #increasing ramp

  with torch.no_grad():
      for c in range(n_steps):
          iteration = dict()
          token_id = []
          token_prob = []
          decoded_tokens = []

          iteration["Input"] = tokenizer.decode(input_ids[0])
          output = model(input_ids=input_ids)

          # Select logits of the first batch and the last token and apply softmax
          next_token_logits = output.logits[0, -1, :]
          next_token_probs = torch.softmax(next_token_logits, dim=-1)

          if use_ramp:
            T_int = TEMP*(1/(1+np.exp(which_ramp*(c-c_o))))
          else:
            T_int = TEMP;

          if T_int < 0.015:
            token_id = torch.argmax(next_token_probs,axis=-1)
          else:
            scaled_probs = next_token_probs**(1/T_int)
            scaled_probs = scaled_probs / scaled_probs.sum()

            token_topk = np.argpartition(scaled_probs.cpu(), -number_to_return)[-number_to_return:]
            for topk in token_topk:
              token_id.append(torch.tensor(topk).cuda())
              decoded_tokens.append(tokenizer.decode(token_id[-1]))
              token_prob.append(next_token_probs[token_id[-1]])
            
            token_choice = dict()
            for token, prob in zip(decoded_tokens, token_prob):
              token_choice[token] = 100 * prob.cpu().item()

          iteration[f"Step {c}"] = token_choice

          # Append predicted next token to input
          top_token_id = torch.argmax(next_token_probs,axis=-1)
          input_ids = torch.cat([input_ids, top_token_id.unsqueeze(0).unsqueeze(0)], dim=-1)

          iterations.append(iteration)
  return iterations

def display_autoregression(iterations: list):
  '''
    Displays the autoregression results, step by step.

      Args:
        iterations: a list containing the input at each step, the chosen token 
                    and probability
      Returns:
        None; prints results
  '''
  print("Token               Percent Probability")
  for iteration in iterations:
    token_prob = iteration['Choice'].split(" (")
    
    if len(token_prob) > 1:
      print(f'{token_prob[0]:20}  {token_prob[1].replace(")","")}')
    else:
      print("help?")

def display_list_probs(iterations: list):
  '''
    Displays the autoregression results, step by step.

      Args:
        iterations: a list containing a dictionary for each step conatins the input at each step, 
                    the top number_to_retun tokens and their probabilities.
      Returns:
        None; prints results
  '''
  for i,iteration in enumerate(iterations):
    print(f"========= Tokens and probabilities for step {i} =========")
    for key in iteration[f"Step {i}"].keys():
      print(f"{key}: {iteration[f'Step {i}'][key]}")    

def setup_encoder(model_name: str):
  '''
    Accepts a model name and loads the tokenizer and a pipeline for the model
      Args:
          model_name: the name of the HF model, in the form user/model

      Returns:
        tokenizer, mask_filler, device
  '''
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  tokenizer = AutoTokenizer.from_pretrained(model_name,padding = True, truncation = True)
  mask_filler = pipeline("fill-mask", model_name)

  return tokenizer, mask_filler, device

def mask_text(raw_text: str, num_to_mask: int):
  '''
    Masks num_to_mask words in the input text

      Args:
        raw_text: input text
        num_to_mask: how many words to mask
      
      Returns:
        output_text: masked text
  '''
  words = raw_text.split()
  mask_idx = random.sample(range(1, len(words)), num_to_mask)
  for idx in mask_idx:
    words[idx] = "[MASK]"

  output_txt = " ".join(words)
  
  return output_txt, mask_idx

def maskfilling_results(result):
  '''
    Displays the tokens and probabilities in the mask-filling results list/dictionary

      Args:
        result: mask-filling results list/dictionary
      
      Returns:
        None; prints results
  '''
  if type(result[0]) == list:
    for i, token in enumerate(result):
      print(f"========= Tokens and probabilities for MASK {i+1} =========")
      for prob in token:
        print(f'Token: {prob["token_str"]:10}, Prob: {100*prob["score"]:5.2f}')
  elif type(result[0]) == dict:
    print(f"========= Tokens and probabilities for MASK 1 =========")
    for i, prob in enumerate(result):
      print(f'Token: {prob["token_str"]:10}, Prob: {100*prob["score"]:5.2f}')
