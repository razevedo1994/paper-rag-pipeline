import langextract as lx
import textwrap
from docling.document_converter import ConversionResult

prompt = textwrap.dedent("""\
""")

examples = [
    lx.data.ExampleData()
]


def extract_metadata(documents: ConversionResult) -> None:
    for document in documents:
        markdown_output = document.document.export_to_markdown()
        first_pages = markdown_output[:6000]
        extraction_result = lx.extract(
            text_or_document=first_pages,
            prompt_description=prompt,
            examples=examples,
            model_id="",
        )

        lx.io.save_annoted_documents(
            [extraction_result], output_name="paper_metadata.jsonl"
        )
