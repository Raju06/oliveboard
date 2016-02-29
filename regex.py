#https://automatetheboringstuff.com/chapter7/

import pyperclip,re

phoneRegex=re.compile(r'''(
	(\d{3}|\(\d{3}\))?					# area code
	(\s|-|\.)?							# separator					
	(\d{3})								# first 3 digits
	(\s|-|\.)							# separator
	(\d{4})								# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?		# extension
	)''',re.VERBOSE)

emailRegex=re.compile(r'''(
	[a-zA-Z0-9._%+-]+					# username
	@									# at the rate symbol
	[a-zA-Z0-9.-]+						# domain name
	(\.[a-zA-Z]{2,4})					# dot-something
	)''',re.VERBOSE)

text=(pyperclip.paste())
text.encode('utf-8')
matches=[]

for groups in phoneRegex.findall(text):
	phoneNum='-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum+= ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')




#The ? matches zero or one of the preceding group.
#The * matches zero or more of the preceding group.
#The + matches one or more of the preceding group.
#The {n} matches exactly n of the preceding group.
#The {n,} matches n or more of the preceding group.
#The {,m} matches 0 to m of the preceding group.
#The {n,m} matches at least n and at most m of the preceding group.
#{n,m}? or *? or +? performs a nongreedy match of the preceding group.
#^spam means the string must begin with spam.
#spam$ means the string must end with spam.
#The . matches any character, except newline characters.
#\d, \w, and \s match a digit, word, or space character, respectively.
#\D, \W, and \S match anything except a digit, word, or space character, respectively.
#[abc] matches any character between the brackets (such as a, b, or c).
