import langextract as lx
import textwrap
from docling.document_converter import ConversionResult

prompt = textwrap.dedent(
    """\
Extract metadata from this technical report including title, all authors, 
affiliation and URLs.
Use exact text from the document.

"Return ONLY a valid JSON object. All values must be strings, numbers, or booleans. Never return null."
"""
)

examples = [
    lx.data.ExampleData(
        text="[Re] Benchmarking LLM Capabilities in Negotiation through Scoreable Games\nJorge Carrasco Pollo\nInformatics Institute University of Amsterdam\nOriginal implementation: https://github.com/S-Abdelnabi/LLM-Deliberation",
        extractions=[
            lx.data.Extraction(
                extraction_class="title",
                extraction_text="[Re] Benchmarking LLM Capabilities in Negotiation through Scoreable Games",
                attributes={},
            ),
            lx.data.Extraction(
                extraction_class="author",
                extraction_text="Jorge Carrasco Pollo",
                attributes={},
            ),
            lx.data.Extraction(
                extraction_class="affiliation",
                extraction_text="Informatics Institute University of Amsterdam",
                attributes={},
            ),
            lx.data.Extraction(
                extraction_class="url",
                extraction_text="https://github.com/S-Abdelnabi/LLM-Deliberation",
                attributes={"type": "repository"},
            ),
        ],
    )
]


def extract_metadata(documents: ConversionResult) -> None:
    for document in documents:
        markdown_output = document.document.export_to_markdown()
        first_pages = markdown_output[:6000]

        try:

            extraction_result = lx.extract(
                text_or_documents=first_pages,
                prompt_description=prompt,
                examples=examples,
                model_id="gemma2:2b",
                model_url="http://localhost:11434",
            )

        except Exception as e:
            print(e)
            raise

        lx.io.save_annoted_documents(
            [extraction_result], output_name="paper_metadata.jsonl"
        )
