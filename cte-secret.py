
import base64
import yaml

# Define inputs
secret_data = {
    'username': 'cte-apprentice',       # input 1
    'password': 'SuperSecret123'        # input 2
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
        'name': 'cte-secret'                                # secret name
    },
    'type': 'Opaque',                                       # Type        
    'data': encoded_data
}

# Write to YAML file
with open('secret.yaml', 'w') as f:                         # Output                
    yaml.dump(k8s_secret, f, default_flow_style=False)

print("secret.yaml created successfully.")