import re

str = "bonjour <text>, test <text>"
print(re.sub('<text>', 'toto', str, 1))