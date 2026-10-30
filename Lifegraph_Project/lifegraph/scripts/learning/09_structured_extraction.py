from pathlib import Path

from pydantic import BaseModel, ConfigDict

from lifegraph.llm.client import client
from lifegraph.llm.config import DEFAULT_MODEL

class Receipt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    merchant: str | None
    transaction_date: str | None

    subtotal_cents: int | None
    tax_cents: int | None
    total_cents: int | None

    payment_method: str | None
    payment_last_four: str | None


receipt_path = Path("tests/receipts/samples/walmart_001.txt").read_text()

response = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[
        {
            "role": "system",
            "content": """
                            You extract financial facts from receipts.

                            Rules:

                            - Extract only information supported by the receipt.
                            - Never guess missing values.
                            - Missing information must be null.
                            - Convert monetary amounts to integer cents.
                            - Convert dates to YYYY-MM-DD when the date is unambiguous.
                      """
        },
        {
            "role": "user",
            "content": receipt_path
        }
    ],
    max_tokens=300,
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "Receipt",

            "strict": True,

            "schema": Receipt.model_json_schema()
        }
    },
    extra_body={
        "provider": {
            "require_parameters": True
        }
    }
)


raw_json = response.choices[0].message.content

print("LLM output:")
print(raw_json)


receipt = Receipt.model_validate_json(raw_json)


print("\nValidated Receipt:")
print(receipt)


print("\nMerchant:")
print(receipt.merchant)

print("\nTotal cents:")
print(receipt.total_cents)