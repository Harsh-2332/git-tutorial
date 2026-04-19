# This will give calls to the fast api of the project.  
# writing logic for calling the api's from hugging face
# code just for the reference
# for using opensource qwen model

try:
    from openai import OpenAI
except ImportError:
    import openai
    OpenAI = openai.OpenAI

# Configured by environment variables
client = OpenAI(api_key="sk-your_dummy_key_here")

messages = [
    {"role": "user", "content": "Type \"I love Qwen3.6\" backwards"},
]

chat_response = client.chat.completions.create(
    model="Qwen/Qwen3.6-35B-A3B",
    messages=messages,
    max_tokens=81920,
    temperature=1.0,
    top_p=0.95,
    presence_penalty=1.5,
    extra_body={
        "top_k": 20,
    }, 
)
print("Chat response:", chat_response)

