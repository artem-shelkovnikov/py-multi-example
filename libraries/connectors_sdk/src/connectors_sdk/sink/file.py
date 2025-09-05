import json
import os

class FileSink:
    def __init__(self, path):
        self._path = path

    def ingest(self, id_, doc):
        os.makedirs(self._path, exist_ok=True)
        with open(f"{self._path}/{id_}", "w") as f:
            f.write(json.dumps(doc, indent=4))

