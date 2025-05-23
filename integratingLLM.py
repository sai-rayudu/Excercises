import requests
headers={
    "Authorization":"Bearer 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",
    "content-Type":"application/json"
}
user_input = input("Give input: ")
data = {
    "model": "mistralai/mistral-7b-instruct",
    "messages": [
        {"role": "user", "content": user_input}
    ]
}

try:
    response=requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=data
    )
    result = response.json()
    print(result['choices'][0]['message']['content'])
except Exception as e:
    print(f"something went wrong{e}")




