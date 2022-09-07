import re

pattern = re.compile(r'm\w\w')

demo_str = "ethod search from re"

result = re.match(pattern, demo_str)

print(result)