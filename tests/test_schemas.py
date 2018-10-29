import json
import os

import jsonschema


def test_all_schemas():
    # Find all the schemas
    schema_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "schemas")
    schema_files = os.listdir(schema_path)

    # Loop through to make sure they are all valid
    for schema_file in schema_files:
        # Test JSONSchemas
        if os.path.splitext(schema_file)[1] == ".json":
            with open(os.path.join(schema_path, schema_file)) as f:
                schema = json.load(f)
            resolver = jsonschema.RefResolver(base_uri="file://{}/".format(schema_path),
                                              referrer=schema)
            validator = jsonschema.Draft4Validator(jsonschema.Draft4Validator.META_SCHEMA,
                                                   resolver=resolver)
            validator.validate(schema)
