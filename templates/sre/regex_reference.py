"""Regex quick reference for SRE interviews."""

import re

# =============================================================================
# QUANTIFIERS
# =============================================================================
# ?     0 or 1
# *     0 or more
# +     1 or more
# {n}   exactly n
# {n,}  n or more
# {n,m} between n and m

# =============================================================================
# CHARACTER CLASSES
# =============================================================================
# .     any char (except newline)
# \d    digit [0-9]
# \D    non-digit
# \w    word char [a-zA-Z0-9_]
# \W    non-word char
# \s    whitespace [ \t\n\r\f]
# \S    non-whitespace
# [abc] any of a, b, c
# [^abc] not a, b, c
# [a-z] range

# =============================================================================
# ANCHORS
# =============================================================================
# ^     start of string
# $     end of string
# \b    word boundary

# =============================================================================
# GROUPS
# =============================================================================
# (...)    capturing group
# (?:...)  non-capturing group
# (?P<name>...) named group

# =============================================================================
# COMMON PATTERNS
# =============================================================================
IP_V4 = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
EMAIL = r"[\w.-]+@[\w.-]+\.\w+"
URL = r"https?://\S+"
TIMESTAMP = r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}"

# =============================================================================
# EXAMPLES
# =============================================================================
if __name__ == "__main__":
    text = '192.168.1.1 - - [2024-01-15T10:30:00] "GET /api" 200'

    # match - from start only
    print(re.match(r"\d+", text))  # <Match '192'>

    # search - anywhere in string
    print(re.search(r"GET", text))  # <Match 'GET'>

    # findall - all matches as list
    print(re.findall(r"\d+", text))  # ['192', '168', '1', '1', '2024', ...]

    # sub - replace
    print(re.sub(r"\d+", "X", "a1b2"))  # aXbX

    # groups
    m = re.search(r'"(\w+) (\S+)"', text)
    if m:
        print(m.group(0))  # "GET /api"
        print(m.group(1))  # GET
        print(m.group(2))  # /api

    # named groups
    m = re.search(r"(?P<method>\w+) (?P<path>\S+)", text)
    if m:
        print(m.group("method"))  # GET
