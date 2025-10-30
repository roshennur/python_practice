import re

# Regex Version of the strip() Method
def regex_strip(text, chars=None):
    if chars is None:
        return re.sub(r'^\s+|\s+$','',text)
    else:
        evil_chars = ""
        for i in chars:
            if i in ".^$*+?{}[]\\|()":
                evil_chars += "\\" + i
            else:
                evil_chars += i

        pattern = f'^[{evil_chars}]+|[{evil_chars}]+$'
        return re.sub(pattern,'',text)

print(regex_strip("$$$Hello, world!$$$", '$'))

