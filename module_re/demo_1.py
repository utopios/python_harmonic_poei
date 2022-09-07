import re

pattern = re.compile(r'm\w\w')

demo_str = "method search from re"

result = pattern.search(demo_str)

print(result.group())