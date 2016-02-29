import re
phoneNumRegex=re.compile(r'Bat(man|mobile|copter|bat)')# backslash is used to escape characters proceeding it
mo=phoneNumRegex.search('Batmobile lost a wheel')
print mo.groups()
print mo.group(1)
print mo.group()
print mo.group(0)