import base64

flag=''
key = "promortyusvatofacidpromortyusvato"
res=base64.b64decode(b'ExMcGQAABzohNQ0TRQwtPidYAS8gXg4kAkcYISwOUQYS',altchars=None)

flag=''.join(chr(ord(a)^ord(b)) for a,b in zip(key,res))
print(flag)
