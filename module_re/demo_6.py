import re

demo_str = "method search from re mrrr"

result = re.findall(r"m\w\w", demo_str)

print(result)