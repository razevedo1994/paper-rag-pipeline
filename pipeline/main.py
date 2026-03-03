from ingestion.document_parser import convert_documents
from ingestion.metadata_extraction import extract_metadata
from config.configs import ARTIFACTS_PATH


def main():

    result = convert_documents(path=ARTIFACTS_PATH)

    extract_metadata(documents=result)


if __name__ == "__main__":
    main()
