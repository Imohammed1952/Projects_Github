import json
from pathlib import Path

from lifegraph.llm.client import client
from lifegraph.llm.config import DEFAULT_MODEL


receipt_text = Path(
    "tests/receipts/samples/walmart_001.txt"
).read_text()

response = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[
        {
            "role": "system",
            "content": """
                            You are a financial document extraction assistant.
                            
                            Extract:
                            - Merchant
                            - Transaction Date
                            - subtotal
                            - tax
                            - total
                            - payment method

                            RULES:
                            1. Do not guess information that is not present in the document.
                            2. If a field is not present, return "N/A" for that field.
                            3. Return monetary values as integer cents
                            4. Convert dates to YYYY-MM-DD.
                            """
        },
        {
            "role": "user",
            "content": receipt_text
        }
    ],
    max_tokens=300,
    response_format={
        "type": "json_scheme"
    }
)

raw_json = response.choices[0].message.content

print("\nRaw JSON:")
print(raw_json)

receipt = json.loads(raw_json)

print("\nPython Object:")
print(receipt)

print("\nTotal:")
print(receipt["total"])