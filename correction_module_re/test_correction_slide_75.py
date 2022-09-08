import re

#1
def replace_str_by_str(first, second, str):
    return re.sub(r"\b"+first+"\b", second, str)

#2
def filter_str_by_per_first_or_end_by_in(liste):
    pattern = r"(^per.*)|(.*in$)"
    return list(filter(lambda str: bool(re.search(pattern,str)), liste))

#3
def replace_by_x_when_start_by_hand_and_word(liste):
    pattern = r"(^hand\w+)"
    return list(map(lambda str: re.sub(pattern, "X", str), liste))


#4
def replace_e_if_hdot(str):
    if re.search(r"^h\.", str):
        return re.sub("e", "X", str)
    return str


def replace_in_list(liste):
    return list(map(replace_e_if_hdot, liste))