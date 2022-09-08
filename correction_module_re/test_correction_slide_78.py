import re


def parse(file):
    data = {}
    with open(file) as reader:
        section = ''
        for line in reader:
            pattern = r'^\[([^[\]]+)\]\s+$'
            match = re.match(pattern, line)
            if(match):
                section = match.group(1)
                continue
            pattern = r'^\s*(.+?)\s*=\s*(.+?)\s*$'
            match = re.match(pattern, line)
            if(match):
                if not data.get(section):
                    data[section] = {}
                data[section][match.group(1)] = match.group(2)
    return data
