translit = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'E',
           'ж':'zh','з':'z','к':'k','л':'l','м':'m','н':'n','о':'o',
            'п':'p','р':'r','с':'c','т':'t','у':'u','ф':'f','х':'h',
            'ц':'c','ч':'ch','ш':'sh','щ':'sch','ь':'^','ы':'y','ъ':'^',
            'э':'e','ю':'ju','я':'ya'}
line = input()
print(line)

text =[]

for i in line:
    text.append(translit.get(i))
    print(''.join(text))
    if line.isupper():
        text.append(translit.get(i)).isupper()
        print(''.join(text))






