with open('ip反查结果.txt','r',encoding='utf-8') as readlist:

    for dirs in readlist.readlines():
        dirs=dirs.split('[aizhan]:')[-1]
        with open('iip.txt','a',encoding='utf-8') as writelist:
                writelist.write('http://'+dirs)
                writelist.write('https://'+dirs)