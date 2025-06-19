# import yaml
# import basecode64


# # 1. secret values
# secret_data = {
#     'username'= 'cte-apprentice'
#     'password' = 'mypass'
# }

# # 2. Encode values to base64 (Kubernetes requires base64)
# encoded_data = {
#     key: base64.b64encode(value.encode()).decode()
#     for key, value in secret_data.items()
# }
# #def encode_base64(value):
#     #return base64.b64encode(value.encode('utf-8')).decode('utf-8')

# # 3. Create K8s Secret Structure
# k8s_secret= {
#     'apiVersion': 'v1',
#     'kind': 'Secret',
#     'metadata': {
#         'name': 'mysecret',
#         'namespace': 'default'
#     }, 
#     'type': 'opaque',
#     'data': enconded_data
#     }
# # 4. Write to YAML file

# with open('secret.yaml', 'w') as file:
#     yaml.dump(k8s_secret, file, default_flow_style=False)

# print("Kubernetes Secret YAML file created successfully: secret.yaml")


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