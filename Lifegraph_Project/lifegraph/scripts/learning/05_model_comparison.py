from lifegraph.llm.client import client

models = [
    "openai/gpt-4.1-mini",
    # Add more later
]

for model in models:
    response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user",
                    "content": "Extract the merchant from: WALMART SUPERCENTER #1234"
                }
        ],
        max_tokens=300
    )

    print("\n\n")
    print(model)
    print(response.choices[0].message.content)
