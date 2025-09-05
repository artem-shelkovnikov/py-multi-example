import requests
from bs4 import BeautifulSoup

from connectors_sdk.base_connector import BaseConnector

class ExternalContributionConnector(BaseConnector):
    @classmethod
    def get_default_configuration(cls):
        return {
            "uri": {
                "label": "Url to fetch",
                "default_value": "https://www.elastic.co",
                "description": "Path to the directory that will be used to sync files from"
            }
        }

    def get_docs(self):
        uri = self._configuration['uri'].get('value') or self._configuration['uri'].get('default_value')


        r = requests.get(uri)

        yield {
            "id": uri,
            "headers": dict(r.headers),
            "text": BeautifulSoup(r.text, features="html.parser").get_text()
        }
