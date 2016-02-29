import re
phoneNumRegex=re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')# backslash is used to escape characters proceeding it
mo=phoneNumRegex.search('My number is (412)-321-3232')
print mo.groups()
print mo.group(1)
print mo.group(2)
print mo.group(0)