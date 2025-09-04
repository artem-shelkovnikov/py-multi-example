class BaseConnector:
    def __init__(self, configuration):
        self._configuration = configuration

    @classmethod
    def get_default_configuration(cls):
        return {}

    def get_docs(self):
        pass
