# ~/.config/qtile/config.py

import json
from jsonschema import validate
from groups import create_groups, create_group_keys, create_rules

# Load schema-config mapping
def load_mapping():
    with open("~/.config/qtile/config_mapping.json", "r") as mapping_file:
        return json.load(mapping_file)

# Validate configurations
def validate_configs(mapping):
    validated_data = {}
    for name, paths in mapping.items():
        with open(paths["schema"], "r") as schema_file:
            schema = json.load(schema_file)
        with open(paths["config"], "r") as config_file:
            config_data = json.load(config_file)
        validate(instance=config_data, schema=schema)
        validated_data[name] = config_data
    return validated_data

# Load and validate configs
mapping = load_mapping()
configs = validate_configs(mapping)

# Retrieve groups, keys, and rules
groups = create_groups(configs["groups"])
group_keys = create_group_keys(configs["groups"])
rules = create_rules(configs["groups"])
