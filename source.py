# -*- coding: utf-8 -*-
import array
import time
print "**************************************************************"
print "*Caesar Cipher based on English Alphabet                     *"
print "*Enter the shift value k to shift the AB and obtain CaesarAB *"
print "**************************************************************"
condition = True
while condition:
    ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def caesar(k):
        abc = []
        for i in range(0,len(ab)-1):
            if i<=len(ab)-k:
                abc.append(ab[i+k-1])
            if i>len(ab)-k and i<len(ab)-1:
                for j in range(0,k-1):
                    abc.append(ab[j])
            if len(abc)>len(ab):
                del abc[len(ab):len(abc)]
        return abc
    k = int(raw_input('Enter k value: '))%26
    abc = caesar(k)
    print "AB : "+str(ab)
    print "CAB : "+str(abc)
    print('Length of AB is '+str(len(ab)))
    print('Length of CaesarAB is '+str(len(abc)))
    enter =raw_input("Type plain text to cipher: ").decode('unicode_escape')
    word = enter.lower()
    word = word.strip()
    cta = list()
    for i in range(0,len(word)):
        if word[i]==' ':
            cta.append(' ')
            continue
        if abc.count(word[i])==0:
            cta.append(word[i])
            continue
        o = ab.index(word[i])
        cta.append(abc[o])
    ct = ''.join(cta)
    print "Plain Text : "+ word
    print "Ciphered Text : "+ct
    ans =raw_input('Would you do another cipher? y/n ')
    if ans=='n':
        condition = False
print "Exiting..."
print "All credits to mattiaquadrini@gmail.com"
time.sleep(3)
