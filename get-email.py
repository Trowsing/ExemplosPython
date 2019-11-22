# Getting email from string

import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w.]+)"
str = "Please contact anything@gmail.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())
