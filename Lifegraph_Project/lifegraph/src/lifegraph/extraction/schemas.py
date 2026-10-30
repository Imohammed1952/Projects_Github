from pydantic import BaseModel, ConfigDict
from datetime import date

class ReceiptItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    description: str
    quantity: int | None
    total_cents: int | None


class Receipt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    merchant: str | None
    transaction_date: date | None
    subtotal_cents: int | None
    tax_cents: int | None
    total_cents: int | None
    currency: str | None
    payment_method: str | None
    payment_last_four: str | None
    items: list[ReceiptItem]