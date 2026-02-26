from ingestion.document_parser import convert_documents
from config.configs import ARTIFACTS_PATH


def main():

    result = convert_documents(path=ARTIFACTS_PATH)

    for document in result:
        print(document.status)


if __name__ == "__main__":
    main()
