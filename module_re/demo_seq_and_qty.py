
import re
str = 'an apple_ a day keeps the doctor away'
result = re.findall(r'a[\w]*', str)

print(result)

result = re.findall(r'\ba[\w]*\b', str)

print(result)

str = 'The meeting will be conducted on 1st and 21st of every month'
result = re.findall(r'\d[\w]*', str)

str = 'one two three four five six seven 8 9 10'
result = re.findall(r'\b\w{5}\b', str)

print(result)