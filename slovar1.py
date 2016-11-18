translit = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'E',
           'ж':'zh','з':'z','к':'k','л':'l','м':'m','н':'n','о':'o', 'и': 'i', 'й': 'ii',
            'п':'p','р':'r','с':'c','т':'t','у':'u','ф':'f','х':'h',
            'ц':'c','ч':'ch','ш':'sh','щ':'sch','ь':'^','ы':'y','ъ':'^',
            'э':'e','ю':'ju','я':'ya'}
line = input()
print(line)

text =[]




for i in line:
    if i.isalpha():
        if i.isupper():
            text.append(translit.get(i.lower()).upper())
        else:
            text.append(translit.get(i))
    else:
        text.append(i)
    print(''.join(text))











