import json
import os

import mdf_toolbox

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__)))))
schema_path = os.path.join(root_path, "schemas")
aux_path = os.path.join(root_path, "connect_aux_data")
docs_path = os.path.dirname(os.path.abspath(__file__))

schema_list = ["dataset", "record", "organization"]
print(root_path)

for schema_name in schema_list:
    with open(os.path.join(schema_path, f"{schema_name}.json")) as f:
        schema_raw = json.load(f)
    with open(os.path.join(docs_path, f"{schema_name}.rst"), 'w') as f:
        # Prepend header
        header = f"MDF {schema_name.capitalize()} Schema"
        f.write(f"{header}\n{'=' * len(header)}\n\n")
        for line in mdf_toolbox.prettify_jsonschema(
                                    mdf_toolbox.expand_jsonschema(schema_raw, schema_path)):
            f.write(line)
            f.write("\n")

with open(os.path.join(aux_path, "organizations.json")) as f:
    org_list_raw = json.load(f)
with open(os.path.join(docs_path, "organizations_list.rst"), 'w') as f:
    header = "MDF Organizations"
    f.write(f"{header}\n{'=' * len(header)}\n")
    for org in org_list_raw:
        f.write(f"\n{org['canonical_name']}\n{'-'*len(org['canonical_name'])}\n\n")
        for line in mdf_toolbox.prettify_json(org, inline_singles=False):
            f.write(line)
            f.write("\n")
