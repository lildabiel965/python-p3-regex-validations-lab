import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = re.compile(r'^[A-Z][a-z]*(?:[- \'][A-Za-z][a-z]*)*$')
name_regex = re.compile(name)

phone_number = re.compile(r"^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$")
phone_regex = re.compile(phone_number)

email_address = re.compile(r"^[a-zA-Z][\w.]+@[a-zA-Z]+\.[a-zA-Z]+$")
email_regex = re.compile(email_address)
