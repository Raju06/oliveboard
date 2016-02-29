import re
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')# backslash is used to escape characters proceeding it
print phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#print mo.groups()
#print mo.group(1)
#print mo.group()
#print mo.group(0)