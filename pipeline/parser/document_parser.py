from docling.document_converter import DocumentConverter


def convert_documents(path: str):
    converter = DocumentConverter()
    result = converter.convert_all(source=path)
    
    return result
