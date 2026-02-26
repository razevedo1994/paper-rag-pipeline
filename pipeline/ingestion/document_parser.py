from docling.document_converter import DocumentConverter


def convert_documents(path: str):
    converter = DocumentConverter()

    input_doc_paths = [
        path / "2602.17831v1.pdf",
        path / "2602.17831v1.pdf",
        path / "2602.18230v1.pdf",
        path / "2602.18372v1.pdf",
        path / "2602.18374v1.pdf",
    ]

    result = converter.convert_all(
        source=input_doc_paths,
        raises_on_error=False,
    )

    return result
