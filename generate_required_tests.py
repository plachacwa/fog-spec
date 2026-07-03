import json
import os

JSON_PATH = os.path.join('build', 'spec_tests_map.json')
OUTPUT_FILE = 'required_tests.txt'
spec_map = ()

if not os.path.exists(JSON_PATH):
    required = []
else:
    with open(JSON_PATH, encoding='utf-8') as f:
        spec_map = json.load(f)
    required = list(spec_map.keys())

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    for spec_id in sorted(required):
        f.write(spec_id + '\n')

print(f"{OUTPUT_FILE} with {len(spec_map)} records has been created.")