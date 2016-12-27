#import random

incorrect = ['врокоа','наокетф','поиврла']
correct = ['корова','конфета', 'правило']

#nagramma = random.choice(incorrect)


#print('Начнем игру \nСоберите слово из - {}'.format(anagramma))
def main():
    for i in range(0, len(incorrect)):
             w = list(incorrect[i])
             while True:
                print(''.join(w))
                command = list(map(int,input().split()))
                lit = w.pop(command[0]-1)
                w.insert(command[1]-1, lit)
                if ''.join(w) == correct[i]:
                 print('ugadal')
                 break
main()





