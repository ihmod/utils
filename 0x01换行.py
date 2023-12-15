##把同一行的ip换行,然后写进result.txt的文件里
# 按','换行
with open('ip.txt','r',encoding='utf-8') as readlist:
    for dirs in readlist.readlines():
         with open('换行-result.txt','a',encoding='utf-8') as writelist:
             b = dirs.replace(" ", '\n')
             writelist.write(b)