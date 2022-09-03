

# Converting a string to JSON format

import json

c3po = """{"name": "C3PO", "height": "167"}"""

c3po = json.loads(c3po)
print(c3po['name'])
print("Type is now", type(c3po))


# Convert back to string

c3po_str = json.dumps(c3po)
print("Type is now", type(c3po_str))
