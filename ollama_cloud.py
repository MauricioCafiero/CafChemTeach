from ollama import Client
import sys
import os
import platform


def get_api_key():
    '''
    Fetch API key based on the operating system.
    - Linux/Mac: Uses environment variable OLLAMA_API_KEY
    - Windows: Uses command line argument or environment variable
    '''
    current_os = platform.system()

    if current_os in ['Linux', 'Darwin']:  # Darwin is macOS
        # Linux/Mac: Use environment variable
        key = os.environ.get('OLLAMA_API_KEY')
        if not key:
            raise ValueError(
                "OLLAMA_API_KEY environment variable not set.\n"
                "Set it with: export OLLAMA_API_KEY='your-api-key'"
            )
        return key

    elif current_os == 'Windows':
        # Windows: Try command line arg first, then environment variable
        if len(sys.argv) > 1:
            key = sys.argv[1]
        else:
            key = os.environ.get('OLLAMA_API_KEY')

        if not key:
            raise ValueError(
                "API key not provided. Either:\n"
                "1. Pass it as a command line argument: python ollama_cloud.py <key>\n"
                "2. Set OLLAMA_API_KEY environment variable"
            )
        return key

    else:
        # Unknown OS: try environment variable as fallback
        key = os.environ.get('OLLAMA_API_KEY')
        if not key:
            raise ValueError(
                f"Unsupported OS: {current_os}. "
                "Set OLLAMA_API_KEY environment variable."
            )
        return key


key = get_api_key()

models = ['deepseek-v3.1:671b', 'deepseek-v3.2', 'gpt-oss:120b', 'gpt-oss:20b', 
          'qwen3:480b', 'qwen3-coder:480b', 'qwen3-vl:235b', 'qwen3.5', 'glm-5', 
          r'glm-4.6', r'kimi-k2.5', 'kimi-k2:1t', 'ministral-3:14b', 'devstral-2:123b', 
          'cogito-2.1:671b']

print('The available cloud models are:')
for i, model in enumerate(models):
    print(f'{i+1}. {model}')
model_choice = int(input('Select the number of the model you would like to use> '))
try:
    model = models[model_choice-1]
except:
    print('Invalid choice. Choosing 3')
    model = models[2]


client = Client(host = 'https://ollama.com',
                headers={'Authorization': f'Bearer {key}'})

messages = []
prompt = ''
print('Welcome to the chat. enter quit to quit.')

while prompt != 'quit':
    prompt = input(f'Talk to {model}:> ')

    if prompt.lower() == 'quit':
        continue

    messages.append({
            'role': 'user', 'content': prompt
        })

    res = client.chat(model, messages=messages)
    answer = res.message.content

    messages.append({
            'role': 'assistant', 'content': answer
        })

    print(answer)

print(f'Thanks for chatting with {model}!')
