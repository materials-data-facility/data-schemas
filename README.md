# data-schemas
This is the repository of Materials Data Facility schemas, in [JSONSchema](https://json-schema.org/) format.

## Access with MDF Forge
Schemas can be accessed in a more human-friendly way via [MDF Forge](https://github.com/materials-data-facility/forge).

To install Forge with `pip`:
```python
pip install mdf-forge
```
To fetch the details of a schema (the `dataset` schema, in this example):
```python
from mdf_forge import Forge
mdf = Forge()
mdf.describe_field("dataset")
```
More details on the `.describe_field()` method can be found in the [Forge documentation](https://mdf-forge.readthedocs.io/en/master/mdf_forge.html#mdf_forge.Forge.describe_field), which includes [examples](https://mdf-forge.readthedocs.io/en/master/tutorials/4-General_Helper_Functions.html#describe_field).

## Reading this repository
Usually, it is not necessary to read these schemas directly. If you want to read the raw JSONSchemas, all of them are in the `schemas` directory. The primary schemas for MDF are `dataset`, `record`, and `connect_submission`, which link to the other schemas using `$ref`. The `dataset` and `record` schemas cover both types of metadata entry in [MDF Search](https://petreldata.net/mdf/?q=*&filter-match-any.mdf.resource_type=dataset), while the `connect_submission` schema covers the JSON payload expected by the [MDF Connect](https://connect.materialsdatafacility.org/) service (the Connect schema is built automatically with the web form or the [MDF Connect Client](https://github.com/materials-data-facility/connect_client)).

# Support
This work was performed under financial assistance award 70NANB14H012 from U.S. Department of Commerce, National Institute of Standards and Technology as part of the Center for Hierarchical Material Design (CHiMaD). 
