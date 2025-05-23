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




