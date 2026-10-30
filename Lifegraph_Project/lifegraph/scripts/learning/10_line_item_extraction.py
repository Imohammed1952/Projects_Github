from lifegraph.llm.client import client
from lifegraph.llm.config import DEFAULT_MODEL

from pathlib import Path

from pydantic import BaseModel, ConfigDict

class ReceiptItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    description: str | None
    quantity: int | None
    total_cents: int | None

class Receipt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    merchant: str | None
    transaction_date: str | None

    subtotal_cents: int | None
    tax_cents: int | None
    total_cents: int | None

    payment_method: str | None
    payment_last_four: str | None

    items: list[ReceiptItem] | None

receipt_text = Path(
    "tests/receipts/samples/normal_receipt.txt"
).read_text(encoding="utf-8")

response = client.chat.completions.create(

    model=DEFAULT_MODEL,
    messages=[
        {
            "role": "system",
            "content": """
                        You extract financial facts from receipts.

                        Rules:
                        - Extract only information explicitly supported by the receipt.
                        - Never guess missing values.
                        - Missing scalar information must be null.
                        - Monetary amounts must be integer cents.
                        - Dates must be YYYY-MM-DD when unambiguous.
                        - Extract purchased line items into the items array.
                        - Do not include SUBTOTAL, TAX, TOTAL, payment lines, or receipt metadata as items.
                        - If there are no identifiable purchased items, return an empty items array.
                        """
        },
        {
            "role": "user",
            "content": receipt_text,
        }
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt",
            "strict": True,
            "schema": Receipt.model_json_schema(),
        }
    },
    max_tokens=300,
    extra_body={
        "provider":{
            "require_parameters": True
        }
    }
)

raw_json = response.choices[0].message.content

print("Raw structured output:")
print(raw_json)

receipt = Receipt.model_validate_json(raw_json)

print("\nValidated receipt:")
print(receipt)

print("\nLine items:")
for item in receipt.items:
    print(
        f"- {item.description}: "
        f"quantity={item.quantity}, "
        f"total_cents={item.total_cents}"
    )
