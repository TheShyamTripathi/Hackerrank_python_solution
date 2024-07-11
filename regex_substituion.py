import re

n = int(input())
lines = [input() for _ in range(n)]
text = "\n".join(lines)

# Perform the replacements
text = re.sub(r'(?<= )&&(?= )', 'and', text)
text = re.sub(r'(?<= )\|\|(?= )', 'or', text)

print(text)
