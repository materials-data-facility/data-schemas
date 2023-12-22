import json
import os
import sys

import globus_sdk

if "API_CLIENT_ID" in os.environ:
    globus_secrets = {
        "API_CLIENT_ID": os.environ["API_CLIENT_ID"],
        "API_CLIENT_SECRET": os.environ["API_CLIENT_SECRET"],
        "smtp_hostname": os.environ["SMTP_HOSTNAME"],
        "smtp_user": os.environ["SMTP_USER"],
        "smtp_pass": os.environ["SMTP_PASS"]
    }
else:
    if len(sys.argv) == 2:
        secret_file = f"./.mdfsecrets.{sys.argv[1]}"
    else:
        secret_file = "./.mdfsecrets"

    with open(secret_file, 'r') as f:
        globus_secrets = json.load(f)

index = "1a57bbe5-5272-477f-9d31-343b8258b7a5"


client = globus_sdk.ConfidentialAppAuthClient(globus_secrets['API_CLIENT_ID'], globus_secrets['API_CLIENT_SECRET'])
cc_authorizer = globus_sdk.ClientCredentialsAuthorizer(client, globus_sdk.SearchClient.scopes.all)

search_client = globus_sdk.SearchClient(authorizer=cc_authorizer)

processed = 0

for page in search_client.paginated.search(index, "*"):
    for result in page.data["gmeta"]:
        print(f"{result['subject']}: {len(result['entries'])}")
        processed += 1

    print(processed)
    if processed > 20:
        break
