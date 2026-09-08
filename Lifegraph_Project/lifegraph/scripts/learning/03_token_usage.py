from lifegraph.llm.client import client

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", 
         "content": "You are a financial document extraction assistant"
        },

        {"role": "user",
         "content": "this is a test to learn about token usage"
        }
    ],
    max_tokens=300
);

print(response.choices[0].message.content);

print("\n\n")
print("Usage:")
print(response.usage)