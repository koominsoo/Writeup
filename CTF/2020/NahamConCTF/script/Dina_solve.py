from pwn import *
code={
'AAA':'a',
'AAC':'b',
'AAG':'c',
'AAT':'d',
'ACA':'e',
'ACC':'f',
'ACG':'g',
'ACT':'h',
'AGA':'i',
'AGC':'j',
'AGG':'k',
'AGT':'l',
'ATA':'m',
'ATC':'n',
'ATG':'o',
'ATT':'p',
'CAA':'q',
'CAC':'r',
'CAG':'s',
'CAT':'t',
'CCA':'u',
'CCC':'v',
'CCG':'w',
'CCT':'x',
'CGA':'y',
'CGC':'z',
'CGG':'A',
'CGT':'B',
'CTA':'C',
'CTC':'D',
'CTG':'E',
'CTT':'F',
'GAA':'G',
'GAC':'H',
'GAT':'J',
'GCA':'K',
'GCC':'L',
'GCG':'M',
'GCT':'N',
'GGA':'O',
'GGC':'P',
'GGG':'Q',
'GGT':'R',
'GTA':'S',
'GTC':'T',
'GTG':'Y',
'GTT':'V',
'TAA':'W',
'TAC':'X',
'TAG':'Y',
'TAT':'Z',
'TCA':'1',
'TCC':'2',
'TCG':'3',
'TCT':'4',
'TGA':'5',
'TGC':'6',
'TGG':'7',
'TGT':'8',
'TTA':'9',
'TTC':'0',
'TTG':' ',
'TTT':'.',
}

r=remote("jh2i.com",50035)
context.log_level='debug'
ss=r.recvline().strip()

flag=''
for i in range(0,len(ss),3):
    flag+=code[ss[i:i+3]]

r.sendafter("> ",flag)
ss=r.recvline().strip()
print(ss)
flag=''
for i in range(0,len(ss),3):
    flag+=code[ss[i:i+3]]
print(flag)

