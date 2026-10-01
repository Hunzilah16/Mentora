with open('topic16_data.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_triple = False
in_double = False
buffer = []

for line in lines:
    stripped = line.strip()
    if '"""' in line or "'''" in line:
        new_lines.append(line)
        continue
    
    # Check if a line opens a double quote that isn't closed
    # Count unescaped double quotes
    quotes = 0
    i = 0
    while i < len(line):
        if line[i] == '"' and (i == 0 or line[i-1] != '\\'):
            quotes += 1
        i += 1
    
    if in_double:
        buffer.append(stripped)
        if quotes % 2 == 1: # closes the open quote
            combined = " ".join(buffer) + "\n"
            new_lines.append(combined)
            buffer = []
            in_double = False
    else:
        if quotes % 2 == 1:
            in_double = True
            buffer.append(line.rstrip('\r\n'))
        else:
            new_lines.append(line)

with open('topic16_data.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed all multiline double quotes!")
