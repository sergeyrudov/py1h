def filework (path1, path2):
    f1 = open(path1)
    f2 = open(path2)
    for element in range(len(f1)):
        print(f1[element])

#filework(r'd:/test/text1.txt',r'd:/test/text2.txt')

password1 = 'Elementary'
password1 = hashlib.sha512(password1.encode('utf-8')).hexdigest()
print (password1)