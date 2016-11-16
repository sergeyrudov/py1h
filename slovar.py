
#translit = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'E',
           'ж':'zh','з':'z','к':'k','л':'l','м':'m','н':'n','о':'o',
            'п':'p','р':'r','с':'c','т':'t','у':'u','ф':'f','х':'h',
            'ц':'c','ч':'ch','ш':'sh','щ':'sch','ь':'^','ы':'y','ъ':'^',
            'э':'e','ю':'ju','я':'ya'}



#a = dict (name = 'nn', familia ='nrr')

line = input()
print(line)

# в строку джоин
text =[]

for i in line:
    text.append(translit.get(i))
    print(''.join(text))






def proverka(a)
   if a%2>0
       print("непарное")
   else:
       print('парное')
    return proverka
