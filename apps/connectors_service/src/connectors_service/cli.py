from time import sleep
from connectors_sdk.utils import create_connector

def main():
    connector_type = "elastic_connectors.filesystem:FilesystemConnector"
    path = "/tmp"
    connector = create_connector(connector_type, { "path": path })

    while True:
        docs = []
        for doc in connector.get_docs():
            docs.append(doc)

        print(f"Size of files in {path} is {sum(x['size'] for x in docs)} bytes")

        sleep(10)


if __name__ == "main":
    main()
