import os
import hashlib

from connectors_sdk.base_connector import BaseConnector

class FilesystemConnector(BaseConnector):
    @classmethod
    def get_default_configuration(cls):
        return {
            "path": {
                "default_value": "/tmp",
                "description": "Path to the directory that will be used to sync files from"
            }
        }

    def get_docs(self):
        path = self._configuration['path'].get('value') or self._configuration['path'].get('default_value')

        for root, dirs, files in os.walk(path):
            for filename in files:
                path = os.path.join(root, filename)
                yield {
                    "id": hashlib.md5(path.encode('utf8')).hexdigest(),
                    "name": filename,
                    "path": path,
                    "size": os.path.getsize(path),
                    "type": "file"
                }
            for dirname in dirs:
                path=os.path.join(root , dirname)
                yield {
                    "id": hashlib.md5(path.encode('utf8')).hexdigest(),
                    "name": dirname,
                    "path": path,
                    "size": sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)),
                    "type": "directory"
                }
