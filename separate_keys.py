import pyperclip,re
text=(pyperclip.paste())

text.encode('utf-8')
print text
vowelRegex = re.compile(r'Answer key: (.*) ')
mo=vowelRegex.search(text)
print mo.group(1)