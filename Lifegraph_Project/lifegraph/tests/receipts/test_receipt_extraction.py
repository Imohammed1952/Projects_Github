import pytest
from pathlib import Path

from lifegraph.extraction.receipt import extract_receipt
from lifegraph.extraction.schemas import Receipt

SAMPLES_DIR = Path("tests/receipts/samples")
EXPECTED_DIR = Path("tests/receipts/expected")

TEST_CASES = [
    "normal_receipt",
    "discount_receipt",
    "missing_total_receipt",
    "no_tax_receipt",
    "partial_information_receipt",
    "walmart_001",
    "walmart_002",
]

@pytest.mark.parametrize("case_name", TEST_CASES)
def test_receipt_extraction(case_name: str):
    # Load receipt text that will be loaded into the llm
    receipt_text = (
        SAMPLES_DIR / f"{case_name}.txt"
    ).read_text(encoding="utf_8")

    # Load expected structured text
    expected_json = (

        EXPECTED_DIR / f"{case_name}.json"
    ).read_text(encoding="utf_8")

    expected_receipt = Receipt.model_validate_json(expected_json)

    # run actual extration pipeline
    actual_receipt = extract_receipt(receipt_text)

    # Compare LLM output to expected result
    assert actual_receipt == expected_receipt

    