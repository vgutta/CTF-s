from PIL import Image
import qrtools
import pyqrcode
poss=[[5],[6,15],[25,2,16],[25,2,16],[25,2,16],[6,15],[26],[3],[4,8,23,24,20],[19,10],[4,20,21,22,23,24],[19,10],[4,20,21,22,23,24],[7],[14,8],[1,18],[23,22,4,24],[23,22,4,24],[23,22,4,24],[1,18],[14,8]]
qr = qrtools.QR()
qr.decode('example.png')
qr.data
poss
univ=[]
import copy
map(len, poss)
univ = list(itertools.product(*poss))
import itertools
univ = list(itertools.product(*poss))
univ[0]
duniv = filter(lambda x: len(set(x)) == len(x), univ)
len(duniv)
univ = duniv
univ[0]
get_ipython().magic(u'ls ')
map(lambda x: str(x)+'.png', univ[0])
list(univ[0])
imgn = list(univ[0])
imgn.sort()
imgn
images = map(Image.open, map(lambda  x: str(x)+'.png', imgn))
images[0]
images = map(Image.open, map(lambda  x: str(x)+'.png', range(27)))
images[0]
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)
total_width
max_height
univ[0]
def tester(tup):
    new_im = Image.new('RGB', (210, 297))
    for i in range(len(tup)):
        new_im.paste(images[tup[i]], (i*10,0))
    new_im.save('test.png')

tester(univ[0])
def isflag():
    if qr.decode('test.png'):
        print qr.data

isflag()
for tup in univ:
    tester(tup)
    isflag()

def isflag():
    if qr.decode('example.png'):
        print qr.data

isflag()
for tup in univ:
    tester(tup)
    isflag()

def isflag():
    if qr.decode('test.png'):
        print qr.data

for tup in univ:
    tester(tup)
    isflag()

len(univ[0])
get_ipython().magic(u'ls ')
univ[0]
tt = list(univ[0])
tt.sort()
tt.sort()
tt
def tester(tup):
    new_im = Image.new('RGB', (270, 297))
    for i in range(len(tup)):
        new_im.paste(images[tup[i]], (i*10,0))
    new_im.save('test.png')

(1, 2, 3) + (5)
(1, 2, 3) + (5, 6)
wuv = map(lambda x: (0, 9, 17) + x + (11, 12, 13), univ)
wuv[0]
for tup in wuv:
    tester(tup)
    isflag()

get_ipython().magic(u'ls ')
wuv[-1]
list(wuv[-1])
len(_)
list(wuv[-1])
len(_)