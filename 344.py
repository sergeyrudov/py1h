import re

text = 'green black red white blue magenta yellow lilack'
text2 = 'Маша родилась 01:07:1991. Вася родился 05/12/1985. Петя родился 06.03.1995.'


pattern  = re.compile(r'\w+ \w+ \d+\.\d+.', re.UNICODE)

print(pattern.findall(text2))