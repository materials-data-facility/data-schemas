import json
import os

import jsonschema


AUX_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "connect_aux_data")
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "schemas")


def test_organizations():
    # Fetch org data
    with open(os.path.join(AUX_PATH, "organizations.json")) as f:
        organizations = json.load(f)
    # Fetch org schema
    with open(os.path.join(SCHEMA_PATH, "organization.json")) as f:
        org_schema = json.load(f)
    resolver = jsonschema.RefResolver(base_uri="file://{}/".format(SCHEMA_PATH),
                                      referrer=org_schema)
    # Check all orgs against org schema (throws jsonschema.ValidationError if invalid)
    [jsonschema.validate(org, org_schema, resolver=resolver) for org in organizations]

    return
