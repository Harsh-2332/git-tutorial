# This will give calls to the fast api of the project.  
# writing logic for calling the api's from hugging face
# code just for the reference
# import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN"
}

payload = {
    "inputs": "What is artificial intelligence?"
}

# response = requests.post(API_URL, headers=headers, json=payload)

# print(response.json())