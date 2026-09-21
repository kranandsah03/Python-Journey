letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''
replace = letter.replace("<|Name|>","Anand Kumar") .replace("<|Date|>", "21st sept 2026")

print (replace)