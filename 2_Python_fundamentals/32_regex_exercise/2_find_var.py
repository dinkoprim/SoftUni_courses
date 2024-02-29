import re

line = input()
pattern = "\\b_([A-Za-z0-9]+)\\b"
matches = re.findall(pattern, line)
print(','.join(matches))
