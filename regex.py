import re
phoneNumRegex=re.compile(r'(Ha){3}')# backslash is used to escape characters proceeding it
mo=phoneNumRegex.search('you are HaHaHa')
#print mo.groups()
#print mo.group(1)
print mo.group()
#print mo.group(0)