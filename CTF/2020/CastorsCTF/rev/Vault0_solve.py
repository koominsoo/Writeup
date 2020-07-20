flag='636173746f72734354467b72317854795f6d316e757433735f67745f73317874795f6d316e757433737d'
def hextostr(x):
    return ''.join(chr(int(''.join(i),16)) for i in zip(*[iter(x)]*2))
print(hextostr(flag))


