import re

pattern = re.compile(r'm\w\w')

demo_str = "method search from re"

result = re.search(pattern, demo_str)

print(result.group())