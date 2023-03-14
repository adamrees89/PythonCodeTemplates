## Credit to Haider Imtiaz
# Parse JSON

import json

# Load JSON File
JSON = open('test.json').read()

# Load JSON String
data = json.loads('{"name": "Bob", "lang": ["En", "Fr"]}')

# Parse JSON
print(data['name'])

# Parse JSON Array
print(data['lang'][0])

# Update JSON
data['name'] = 'Alice'

# Add new key
data['age'] = 20

# Write JSON
with open('test.json', 'w') as f:
    json.dump(data, f)

# Write JSON with Formatting
with open('test.json', 'w') as f:
    json.dump(data, f, indent=4)