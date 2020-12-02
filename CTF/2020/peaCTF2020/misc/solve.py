from PIL import Image
im=Image.open(".\\hehe.png")
img=im.convert("RGBA")
datas=img.getdata()
newData=[]
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((255,255,255,0))
    else:
        newData.append(item)

img.putdata(newData)
img.save(".\\out.png","PNG")