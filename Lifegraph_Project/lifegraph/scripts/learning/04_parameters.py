from lifegraph.llm.client import client

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system",
          "content": "You are a financial document extraction assistant"
        },

        {"role": "user",
         "content": "This is a test on parameters and temperature."
        }
    ],
    max_tokens=300,
    temperature=0.7
)

print("\nResponse:")
print(response.choices[0].message.content)