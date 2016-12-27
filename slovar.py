import random

anagramma = ("корова","правило","конфета",)
# случайным образом выбираем из последовательности одно слово
word = random.choice(anagramma)
# Создадим переменную, с которой будет сопоставлена версия игрока
correct = word

# создаем анаграмму выбранного слова, в которой буквы будут расставлены хаотично
mixed = ""
while word:
    position = random.randrange(len(word))
    mixed+= word[position]
    word = word[:position] + word[(position + 1):]



print("Начинаем игру")
print("Вот анаграмма: {}".format(mixed))
ugadal = input("Попробуйте отгадать исходное слово: ")
while ugadal != "" and ugadal != correct:
    if ugadal != correct:
        print("К сожалению, вы неправы.")
    if ugadal == correct:
        print("Да, именно так! Вы отгадали!")

# Если игрок слишком часто использовал подсказку (что странно, ведь она одна и та же), избегаем отрицательного значения
# приводя к нулю







