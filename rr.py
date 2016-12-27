#a = ['У', 'Матери', 'есть', 'маленькая', 'овечка','hheher']
#for i in range(len(a)):
#    print (i)
def filework (path1, path2,path3):
    f1 = open(path1)
    f2 = open(path2)
    ff2 = f2.readlines()
    ff1 = f1.readlines()

    f3 = open(path3,'w')



    if len(ff1) <= len(ff2):
        r = range(0, len(ff1))
    else:
        r = range(0, len(ff2))

    for element in r:
        if ff1[element] == ff2[element]:
            print (element)
            f3.write("({0}): {1}".format(element, ff2[element]))
    f3.close()

filework(r'd:/test/text1.txt', r'd:/test/text2.txt',r'd:/test/text3.txt')

