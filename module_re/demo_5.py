import re

str = "bonjour <tExt>, test <text>"
print(re.sub('<text>', 'toto', str, flags=re.IGNORECASE))