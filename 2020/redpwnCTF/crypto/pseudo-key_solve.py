from string import ascii_lowercase
import random
import time
cyp="z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"
key="iigesssaemk"
okey=[]

p=[('a', 'n'), ('b', 'o'), ('c', 'p'), ('d', 'q'), ('e', 'r'), ('f', 's'), ('g', 't'), ('h', 'u'), ('i', 'v'), ('j', 'w'), ('k', 'x'), ('l', 'y'), ('m', 'z')]

for i in range(50):
    t=''
    random.seed(time())
    for j in range(len(key)):
        t+=chr((ord(p[j][random.random()%2])-97))
    okey.append(t)

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

def decrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x - y) % 26]
    return ctxt

for i in range(50):
    print('key : %s, flag = %s'%(okey[i],decrypt(cyp,okey[i])))
