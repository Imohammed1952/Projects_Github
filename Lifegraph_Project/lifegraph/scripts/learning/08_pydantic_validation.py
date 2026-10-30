from pydantic import BaseModel, ConfigDict

class Receipt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    merchant: str | None
    transaction_date: str | None

    subtotal: int | None
    tax: int | None
    total_cents: int | None

    payment_method: str | None
    payment_last_four: str | None

data = {
    "merchant": "WALMART SUPERCENTER #1234",
    "transaction_date": "2023-08-15",
    "subtotal": 12345,
    "tax": 678,
    "total_cents": 13023,
    "payment_method": "CREDIT CARD",
    "payment_last_four": "5678",
}

receipt = Receipt.model_validate(data)
print()
print(receipt)
print()
print(receipt.merchant)
print()
print(receipt.total_cents)