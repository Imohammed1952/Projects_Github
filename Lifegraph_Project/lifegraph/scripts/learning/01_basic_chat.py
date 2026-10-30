from lifegraph.llm.client import client

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", 
         "content": "What is the difference between a reciept and an invoice?"
         }
    ],
    max_tokens=300
);


print(response.choices[0].message.content);