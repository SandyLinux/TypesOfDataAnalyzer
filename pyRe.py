import re
txt1= 'Thesw3eorwueo5'

ret = re.search('\d',txt1)
print(ret)

str = "The  rain in Spain"
x = re.split("\s", str)


str = "The rain in Spain"
x = re.sub("\s", "9", str)

m = re.search('(?<=abc)def', 'abcdef')
m = re.search('(?<=-)\w+', 'spam-egg')

pattern1 = re.compile("^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$")
p1 = re.compile('(?!b)bc')

b = re.compile(r"\d+.\d*")
m = re.match(b, '12.12212')
m=re.subn('-{1,2}', '/','pro----gram-files')
x=re.escape('?')
m=re.match(x, '?e?we')
print(re.escape('?'))

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
ret = re.search('w\d', txt1)

print(txt1[ret.end()])
