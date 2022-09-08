import re

content = '''start line
not
with stArt
hello from line'''

def get_line_with_out_start(text):
    pattern = re.compile(r'start', flags=re.IGNORECASE)
    lines = re.split('\n', text)
    result = []
    for line in lines:
        if not pattern.search(line):
            result.append(line)
    return result

def test_get_line_with_out_start():
    result = get_line_with_out_start(content)
    assert result == ['not', 'hello from line']