import re

# prath12@gmail.com
try:
    with open('random_emails_text.txt') as fh:
        content = fh.read()
        pattern = r"[0-9 a-z A-Z . _]+@[a-z]+.[a-z]{2,3}"
        emails = re.findall(pattern, content)
        print(emails)
        print(f"emails list count:{len(emails)}")
except FileNotFoundError as e:
    print(f"File not found: {e}")