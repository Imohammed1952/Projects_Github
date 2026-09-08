from pathlib import Path

from lifegraph.llm.client import client
from lifegraph.llm.config import DEFAULT_MODEL

receipt_text = Path(
    "tests/receipts/samples/walmart_002.txt"
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

                            Do not guess information that is not present in the document. If a field is not present, return "N/A" for that field.
                      """
        },
        {
            "role": "user",
            "content": receipt_text
        }
    ],
    max_tokens=300
)

print(response.choices[0].message.content)