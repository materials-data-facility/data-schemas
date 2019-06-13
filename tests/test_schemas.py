import json
import os

import jsonschema
import pytest


SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "schemas")
TEST_FILES_PATH = os.path.join(os.path.dirname(__file__), "test_files")


def test_basic_validation():
    # Loop through all schemas to make sure they are all valid
    for schema_file in os.listdir(SCHEMA_PATH):
        # Test JSONSchemas
        if os.path.splitext(schema_file)[1] == ".json":
            with open(os.path.join(SCHEMA_PATH, schema_file)) as f:
                schema = json.load(f)
            resolver = jsonschema.RefResolver(base_uri="file://{}/".format(SCHEMA_PATH),
                                              referrer=schema)
            validator = jsonschema.Draft4Validator(jsonschema.Draft4Validator.META_SCHEMA,
                                                   resolver=resolver)
            validator.validate(schema)


def test_sample_validation():
    jsonschemas_to_test = [
        "dataset",
        "record",
        "connect_submission",
        "internal_status"
    ]
    for schema_name in jsonschemas_to_test:
        # Get schema
        with open(os.path.join(SCHEMA_PATH, schema_name+".json")) as f:
            schema = json.load(f)
        resolver = jsonschema.RefResolver(base_uri="file://{}/".format(SCHEMA_PATH),
                                          referrer=schema)

        # Run all test cases
        test_files_dir = os.path.join(TEST_FILES_PATH, schema_name)
        for test_file in os.listdir(test_files_dir):
            with open(os.path.join(test_files_dir, test_file)) as t:
                test_case = json.load(t)
            # Success cases start with "success", failure cases start with "failure"
            if test_file.startswith("success"):
                jsonschema.validate(test_case, schema, resolver=resolver)
            elif test_file.startswith("failure"):
                with pytest.raises(jsonschema.ValidationError):
                    jsonschema.validate(test_case, schema, resolver=resolver)
            else:
                print("Skipping test file '{}'".format(test_case))
