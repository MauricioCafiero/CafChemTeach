import ollama
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

vector_store_flag = False

def get_model_list():
    '''
    Returns a list of available ollama models.

      Args:
        None
      Returns:
        matches: a list of available model names
    '''
    models_list = ollama.list()
    models_list = str(models_list)

    model_pattern = r'model=\'[A-Za-z0-9\.]*\:[A-Za-z0-9]*'
    matches = re.findall(model_pattern, models_list)

    matches = [m.replace("model='", "") for m in matches]

    return matches

def custom_model():
    base_model_idx = int(input('Choose a base model from the options above: '))
    base_model = models[base_model_idx-1]

    temp = float(input('Choose a model temperature between 0 and 2: '))

    personality = input('Enter a sentence or two describing the personality you want your model to have: ')
    model_name = input('Enter a name for your model: ')

    model_file = f'''
    PARAMETER temperature {temp}
    SYSTEM {personality}
    '''

    ollama.create(model = model_name, system = model_file, from_ = base_model.split(':')[0] )

    print(f'{model_name} has been created!')
    return model_name

def prep_vector_store(filename):
    '''
    Loads a PDF file, splits it into chunks, and creates a Chroma vector store.

      Args:
        filename: path to the PDF file to load
      Returns:
        vector_store: a Chroma vector store containing the document chunks
    '''
    global vector_store_flag
    vector_store_flag = True
    loader = PyPDFLoader(filename)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    chunks = text_splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model= 'embeddinggemma:300m')
    vector_store = Chroma.from_documents(chunks, embeddings)

    return vector_store

def chat_with_doc(vector_store,query):
    '''
    '''
    retriever = vector_store.as_retriever(searh_type = 'similarity',
                                           search_kwargs = {'k': 4})
    docs = retriever.invoke(query)
    if not docs:
        docs = None
    
    try:
        just_content = [doc.page_content for doc in docs]
        print('Finished searching the document.')
    except:
        just_content = ['']

    return just_content

models = get_model_list()
print('Choose a model:')
for i,model in enumerate(models):
    print(f'{i+1}. {model}')
print('99. Create a custom model.')
model_idx = input('Choice:>')
model_idx = int(model_idx)

if model_idx != 99:
    model = models[model_idx-1].split(':')[0]
    print(f'Using model: {model}')
else:
    model = custom_model()


messages = []
prompt = ''
print('Welcome to the chat. enter quit to quit\nTo read in a PDF, enter: \
PDF> filename. \nTo chat with the PDF, enter: RAG> your query.')

while prompt != 'quit':
    prompt = input(f'Talk to {model}:> ')

    if prompt.lower() == 'quit':
        continue

    if 'PDF>' in prompt:
        filename = prompt.split('>')[1].strip()
        vector_store = prep_vector_store(filename)
        continue
    
    if ('RAG>' in prompt) and (vector_store_flag):
        prompt = prompt.split('>')[1].strip()
        context = chat_with_doc(vector_store, prompt)
        prompt_with_context = f'Answer the question using only the CONTEXT as source material. \
Question: {prompt} \n CONTEXT: {'\n'.join(context)}'
        prompt = prompt_with_context

    messages.append({
            'role': 'user', 'content': prompt
        })

    res = ollama.chat(
        model = model,
        messages = messages
    )
    answer = res['message']['content']

    messages.append({
            'role': 'assistant', 'content': answer
        })

    print(answer)

print(f'Thanks for chatting with {model}!')