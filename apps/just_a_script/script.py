from elastic_connectors.filesystem import FilesystemConnector
from connectors_sdk.sink.file import FileSink

configured_connector_path =   "/Users/artemshelkovnikov-m2/git_tree/connectors-sources-infra"
sink_dir = "/tmp/ingest"

connector = FilesystemConnector({'path': {'value': configured_connector_path}})
sink = FileSink(sink_dir)

print(f"Ingesting docs to ${sink_dir}")

for doc in connector.get_docs().limit(10):
    print(f"Ingesting doc {doc['id']}")
    id_ = doc.pop('id', None)
    sink.ingest(id_, doc)

print(f"Done ingesting, go check ${sink_dir}")
