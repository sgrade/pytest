import yaml


def parse_yml(config="loader.yml"):
    """
    Creates a dictionary from config file
    :type config: string
    :rtype: dictionary
    """
    with open(config) as yml_file:
        dictionary = yaml.safe_load(yml_file)
        return dictionary
