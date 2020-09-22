import re
[print('Valid') if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$', input()) else print('Invalid') for _ in range(int(input()))]





# Explanation:

# (?!.*(.).*\1) checks no repeating characters;
# (?=(?:.*[A-Z]){2,}) checks at least 2 uppercase letters;
# (?=(?:.*\d){3,}) checks at least 3 digits;
# [a-zA-Z0-9]{10} checks exactly 10 alphanumeric characters.