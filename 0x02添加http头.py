# 判断有没有http头，有跳过，没有统一加上http
# 去重
# 漏洞批量测试时使用
with open('ip.txt','r',encoding='utf-8') as readlist:
    lines_seen = set()
    for dirs in readlist.readlines():
        flag=dirs[0:5]=='https' or dirs[0:5]=='http:'
        if flag==False:
            dirs  = 'http://'+dirs  
        if dirs not in lines_seen:
            lines_seen.add(dirs)         
            with open('添加http-result.txt','a',encoding='utf-8') as writelist:
                writelist.write(dirs)