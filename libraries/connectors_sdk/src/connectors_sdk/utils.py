import importlib

def get_connector_configuration(fqn):
    connector_class = __get_connector_class(fqn)

    default_configuration = connector_class.get_default_configuration()

    return default_configuration

def create_connector(fqn, configuration):
    connector_class = __get_connector_class(fqn)

    default_configuration = connector_class.get_default_configuration()

    for key, value in configuration.items():
        default_configuration[key]["value"] = value

    return connector_class(default_configuration)

def __get_connector_class(fqn):
    module_name, class_name = fqn.split(':')
    module = importlib.import_module(module_name)
    actual_class = getattr(module, class_name)
    
    return actual_class
