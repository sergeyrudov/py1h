import random
anagramma = ('корова','правило','конфета',)
# случайным образом выбираем из последовательности одно слово
word = random.choice(anagramma)
correct = word

# создаем анаграмму выбранного слова, в которой буквы будут расставлены хаотично
mixed = ""
while word:
    position = random.randrange(len(word))
    mixed+= word[position]
    word = word[:position] + word[(position + 1):]
print(mixed)