import zipfile
import os

base=os.path.dirname(os.path.realpath(__file__))

fantasy_zip = zipfile.ZipFile(base+'\\layer1000.zip')
fantasy_zip.extract('layer999.zip', base)
for i in range(999,0,-1):
    z=zipfile.ZipFile(base+f'\\layer{i}.zip')
    z.extract(f'layer{i-1}.zip',base)
print(base)