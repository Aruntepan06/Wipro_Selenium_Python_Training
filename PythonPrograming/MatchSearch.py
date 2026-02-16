# match - match the exact sequence

import re

# o/p match object
text = "hello world"
result = re.match("hello", text)

print(result)

#using pattern:

import re

# using pattern
test_str = "123566778abcghhhjhjabcABC"
pattern = re.compile("abc")

matches = pattern.finditer(test_str)

for match in matches:
    print(match)

import re

# returns the first occurrence
text = "python of powerful maths powerful"
result = re.search("powerful", text)

print(result)


#raw string

a = "\tHello"
print(a)

# match()  - Determine if the RE matches at the beginning of the string.
# search() - Scan through a string, looking for any location where this RE matches.
# finditer() - Find all substrings where the RE matches, and returns them as an iterator.
# findall() - Find all the strings where the RE matches and returns a list.

my_string = "abc123ABC123abc"
pattern = re.compile(r'123')

matches = pattern.findall(my_string)

for match in matches:
    print(match)
import re

# Methods on match object:
# group() - Return the string matched by the RE
# start() - Return the starting position of the match
# end()   - Return the ending position of the match
# span()  - Return a tuple containing the (start, end) positions


test_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')

matches = pattern.finditer(test_string)

for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group())  # return the substring that was matched by the RE

# special characters
# meta characters
# regular expressions

# Pattern      Meaning
# abc          Matches exact text
# [abc]        a or b or c
# [a-z]        lowercase letters
# [0-9]        digits
# a|b          a or b
# .            Any single character
# abc → matches exact text
text = "I like abc and abcde"
result = re.findall("abc", text)
print(result)

# [abc] → a or b or c (matches any one of these characters)
text = "apple banana cat"
result = re.findall("[abc]", text)
print(result)

# [a-z] → lowercase letters
text = "I like abc and ABCGHJHJH"
result = re.findall("[a-z]", text)
print(result)

# [0-9] → digits
text = "I like abc and 123455ABCGHJHJH"
result = re.findall("[0-9]", text)
print(result)

import re

# Matches either "cat" OR "bat"
text = "cat bat rat mat"
result = re.findall("cat|bat", text)
print(result)

# . → any single character
text = "cat bat rat bob"
result = re.findall("c.t", text)   # matches cat
result1 = re.findall(".r.", text)  # matches rat

print(result)
print(result1)



# Special Sequences (start with backslash \)

# \d  → Digit (0–9)
# \D  → Non-digit
# \w  → Word character (a–z, A–Z, 0–9, _)
# \W  → Non-word character
# \s  → Whitespace (space, tab, newline)
# \S  → Non-whitespace
# \b  → Word boundary
# \B  → Not a word boundary


# Example for \d (digits)
text = "Order 123 costs 450"

result = re.findall(r"\d", text)   # finds all digits
print("Digits:", result)


# Example for \D (non-digits)
result = re.findall(r"\D", text)
print("Non-Digits:", result)


# Example for \w (word characters)
result = re.findall(r"\w", text)
print("Word characters:", result)


# Example for \W (non-word characters)
result = re.findall(r"\W", text)
print("Non-word characters:", result)


# Example for \s (whitespace)
result = re.findall(r"\s", text)
print("Whitespace:", result)


# Example for \S (non-whitespace)
result = re.findall(r"\S", text)
print("Non-whitespace:", result)


# Example for \b (word boundary)
text2 = "cat scatter cater cat"
result = re.findall(r"\bcat\b", text2)   # matches only full word 'cat'
print("Word boundary:", result)


# Example for \B (not a word boundary)
result = re.findall(r"\Bcat", text2)   # matches 'cat' inside words
print("Not word boundary:", result)

#for all the Meta Deta


# ^  Start of string
text = "Python is easy"
print(re.findall(r"^Python", text))


# $  End of string
text = "Python is easy"
print(re.findall(r"easy$", text))


# *  0 or more
text = "ab abb abbb a"
print(re.findall(r"ab*", text))


# +  1 or more
text = "ab abb abbb a"
print(re.findall(r"ab+", text))


# ?  0 or 1
text = "color colour colr"
print(re.findall(r"colou?r", text))


# {n}  Exactly n times
text = "aaa aa aaaa"
print(re.findall(r"a{3}", text))


# {n,}  n or more times
text = "aaa aa aaaaa"
print(re.findall(r"a{3,}", text))


# {n,m}  Between n and m times
text = "a aa aaa aaaa"
print(re.findall(r"a{2,3}", text))


# |  OR operator
text = "cat bat rat"
print(re.findall(r"cat|bat", text))


# []  Character set
text = "apple banana cat"
print(re.findall(r"[abc]", text))


# .  Any single character
text = "cat bat rat"
print(re.findall(r"c.t", text))


# \d  Digit
text = "Price 500"
print(re.findall(r"\d", text))

# Regular expression modifiers
'''
Modifier           Short   Purpose
re.IGNORECASE      re.I    Case-insensitive matching
re.MULTILINE       re.M    ^ and $ match each line
re.DOTALL          re.S    . matches newline
re.VERBOSE         re.X    Write readable regex with comments
re.ASCII           re.A    ASCII-only matching
re.DEBUG           -       Debug pattern
'''



# re.IGNORECASE  (re.I) → Case-insensitive matching
text = "Python"
print(re.search("python", text, re.I))


# re.MULTILINE  (re.M) → ^ and $ match each line
text = "Hello\nPython"
print(re.findall("^Python", text, re.M))


# re.DOTALL  re.S  . matches newline

text = "Hello\nWorld"
print(re.search("Hello.*World", text, re.S))


# re.VERBOSE  re.X  Write readable regex with comments - make it more readable


pattern = re.compile(r"""
    7879hbgjklksdgdskl..%^^&*&89
""", re.X)

print(pattern)


# re.ASCII  re.A  ASCII-only matching
print(re.findall(r"\w+", text, re.A))


# re.DEBUG  –  Debug pattern
pattern = re.compile(r"""
    7879hbgjklksdgdskl..%^^&*&89
""", re.DEBUG)

print(pattern)

"""""
^  → Start of string
$  → End of string
\b → Word boundary
\B → Not word boundary
(?=...)  → Positive Lookahead
(?!...)  → Negative Lookahead
(?<=...) → Positive Lookbehind
(?<!...) → Negative Lookbehind
"""
# ^ → Start of string
print(re.findall(r"^Hello", text))

# $ → End of string
print(re.findall(r"cat123$", text))

# \b → Word boundary (whole word match)
print(re.findall(r"\bcat\b", text))

# \B → Not word boundary (inside word)
print(re.findall(r"\Bcat\B", text))

# (?=...) → Positive Lookahead = match only if followed by something
text = "user1 admin2 test"
print(re.findall(r"\w+(?=\d)", text))


# (?!...) → Negative Lookahead
text = "user1 admin test2"
print(re.findall(r"\b(?!\d)\w+\b", text))


# (?<=...) → Positive Lookbehind (cat preceded by digit)
print(re.findall(r"(?<=\d)cat", text))


# (?<!...) → Negative Lookbehind (cat not preceded by digit)
print(re.findall(r"(?<!\d)cat", text))