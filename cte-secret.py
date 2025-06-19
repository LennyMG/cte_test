
import base64
import yaml

# Define the secret values
secret_data = {
    'username': 'cte-apprentice',
    'password': 'SuperSecret123'
}

# Encode the values using base64
encoded_data = {
    key: base64.b64encode(value.encode()).decode()
    for key, value in secret_data.items()
}

# Build the Kubernetes Secret dictionary
k8s_secret = {
    'apiVersion': 'v1',
    'kind': 'Secret',
    'metadata': {
        'name': 'cte-secret'
    },
    'type': 'Opaque',
    'data': encoded_data
}

# Write to YAML file
with open('cte-secret.yaml', 'w') as f:
    yaml.dump(k8s_secret, f, default_flow_style=False)

print("cte-secret.yaml created successfully.")