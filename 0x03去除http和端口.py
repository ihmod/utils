# 去除http头和端口号
#去重
# ip反查前处理
with open('ip.txt','r',encoding='utf-8') as readlist:
    lines_seen = set()
    for dirs in readlist.readlines():
        dirs=dirs.split('//')[-1]
        if ':' in dirs:
            dirs=dirs.split(':')[0]+'\n'
        if dirs not in lines_seen:
            lines_seen.add(dirs)         
            with open('待ip反查.txt','a',encoding='utf-8') as writelist:
                writelist.write(dirs)