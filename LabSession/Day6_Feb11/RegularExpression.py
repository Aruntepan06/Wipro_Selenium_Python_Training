import re

# 1. Check if string contains only digits
print(bool(re.fullmatch(r"\d+", "123456")))

# 2. Match a 10-digit mobile number
print(bool(re.fullmatch(r"\d{10}", "9876543210")))

# 3. Find all lowercase letters
print(re.findall(r"[a-z]", "Hello ABC def"))

# 4. Extract all uppercase letters
print(re.findall(r"[A-Z]", "Hello ABC def"))

# 5. Match string that starts with "Hello"
print(bool(re.search(r"^Hello", "Hello world")))

# 6. Match string that ends with "world"
print(bool(re.search(r"world$", "Hello world")))

# 7. Find all words separated by spaces
print(re.findall(r"\w+", "Python is very easy"))

# 8. Match exactly 5 characters
print(bool(re.fullmatch(r".{5}", "Hello")))

# 9. Find all occurrences of "python" (case-sensitive)
print(re.findall(r"python", "python is fun. python code. Python"))

# 10. Replace all spaces with underscores
text = "Python is fun"
print(re.sub(r"\s", "_", text))
