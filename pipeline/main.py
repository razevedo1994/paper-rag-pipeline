from parser.document_parser import convert_documents
from pathlib import Path


def main():
    data_folder = Path(__file__).parent / "artifacts"

    input_doc_paths = [
        data_folder / "2602.17831v1.pdf",
        data_folder / "2602.17831v1.pdf",
        data_folder / "2602.18230v1.pdf",
        data_folder / "2602.18372v1.pdf",
        data_folder / "2602.18374v1.pdf",
    ]

    result = convert_documents(path=input_doc_paths)

    for document in result:
        print(document.status)


if __name__ == "__main__":
    main()
