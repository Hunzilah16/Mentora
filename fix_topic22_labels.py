import re

with open('build_topic22_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "part": "1(a)" or "part": "46(d)" with "part": "(a)" or "part": "(d)"
new_content = re.sub(r'"part":\s*"\d+\(([a-z]+)\)"', r'"part": "(\1)"', content)

with open('build_topic22_data.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated build_topic22_data.py successfully!")
