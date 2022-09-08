import json

from correction_module_re.test_correction_ex_slide_76 import question_5
from correction_module_re.test_correction_slide_78 import parse

question_5()

###Test ex slide 78
with open("result.json", 'w') as writer:
    json.dump(parse("a.ini"), writer)