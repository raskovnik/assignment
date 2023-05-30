import re

text = "Hello Hello, Howdy Howdy Hi Hi"

#sub - used to find a substring where a regex pattern matches, and then it replaces the matched substring with a different string
new_text = re.sub(r"Hello", "hello", text);
print(f"New text after substitution: {new_text}")

# subn - same as the re.sub() function, except that it also provides a count of the number of replacements that it has done.
new_text, count = re.subn(r"Howdy", "howdy", text);
print(f"New text after substitution: {new_text}\nNumber of substitutions: {count}")


def verify_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else: print(f"{email} is not a valid email address")

emails = ["user@example.com", "invalid.email", "another@domain.co"]

for email in emails:
    verify_email((email))