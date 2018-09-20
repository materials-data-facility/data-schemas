from jsonschema import Draft4Validator, RefResolver
import json
import glob
import os

# Find all the schemas
schema_path = os.path.abspath('.')
schemas = glob.glob('{}/**/*.json'.format(schema_path), recursive=True)

# Loop through to make sure they are all valid
for schema in schemas:
    print('Checking {}...'.format(os.path.relpath(schema, '.')), end="")

    # Load in the schema
    with open(schema) as fp:
        schema = json.load(fp)

    # Pull in the references
    validator = Draft4Validator(Draft4Validator.META_SCHEMA,
                                resolver=RefResolver('file:///{}/'.format(schema_path), schema))
    validator.validate(schema)
    print('OK')
