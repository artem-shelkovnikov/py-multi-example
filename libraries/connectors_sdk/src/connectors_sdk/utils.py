import importlib

def create_connector(fqn, configuration):
    module_name, class_name = fqn.split(':')
    module = importlib.import_module(module_name)
    actual_class = getattr(module, class_name)

    default_configuration = actual_class.get_default_configuration()

    for key, value in configuration.items():
        default_configuration[key]["value"] = value

    return actual_class(default_configuration)
