from connectors_sdk.utils import create_connector

def main():
    connector_type = "elastic_connectors.filesystem:FilesystemConnector"
    connector = create_connector(connector_type, { "path": "/tmp" })

    for doc in connector.get_docs():
        print(f"Got a doc:\n{doc}")


if __name__ == "main":
    main()
