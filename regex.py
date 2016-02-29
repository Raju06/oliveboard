import re
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search('My number is 412-321-3232')
print ('Phone no. found: '+mo.group())