from lifegraph.llm.client import client
from lifegraph.llm.config import DEFAULT_MODEL
from lifegraph.extraction.schemas import Receipt


SYSTEM_PROMPT = """
You extract structured financial information from receipts.

Rules:
- Never invent missing information.
- Use null when a value cannot be determined.
- Return monetary amounts in integer cents.
- Extract only facts supported by the receipt text.
""".strip()


def extract_receipt(receipt_text: str, model: str = DEFAULT_MODEL) -> Receipt:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": receipt_text},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "receipt",
                "strict": True,
                "schema": Receipt.model_json_schema(),
            },
        },
        extra_body={
            "provider": {
                "require_parameters": True,
            }
        },
        max_tokens=300,
    )

    raw_json = response.choices[0].message.content
    return Receipt.model_validate_json(raw_json)
