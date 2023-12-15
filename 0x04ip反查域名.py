
#-- coding:UTF-8 --
import re, time
from urllib.parse import urlparse
import requests
from fake_useragent import UserAgent
from tqdm import tqdm
import os

# 爱站
def aizhan_chaxun(ip, ua):
    aizhan_headers = {
        'Host': 'dns.aizhan.com',
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://dns.aizhan.com/'}
    aizhan_url = 'https://dns.aizhan.com/' + str(ip) + '/'
    try:
        aizhan_r = requests.get(url=aizhan_url, headers=aizhan_headers, timeout=2).text
        aizhan_nums = re.findall(r'''<span class="red">(.*?)</span>''', aizhan_r)
        if int(aizhan_nums[0]) > 0:
            aizhan_domains = re.findall(r'''rel="nofollow" target="_blank">(.*?)</a>''', aizhan_r)
            return aizhan_domains
    except:
        pass

def catch_result(i):
    ua_header = UserAgent()
    i = i.strip()
    if "http://" not in i:
        i="http://"+i
    try:
        ip = urlparse(i).netloc
        aizhan_result = aizhan_chaxun(ip, ua_header)
        time.sleep(1)
        if (aizhan_result != None ):
            with open("ip反查结果.txt", 'a') as f:
                result = "[url]:" + i + "   " +  "  [aizhan]:" + str(aizhan_result[0])
                print(result)
                f.write(result + "\n")
        else:
            with open("反查失败列表.txt", 'a') as f:
                f.write(i + "\n")
    except:
        pass


if __name__ == '__main__':
    url_list = open("待ip反查.txt", 'r').readlines()
    url_len = len(open("待ip反查.txt", 'r').readlines())
    #每次启动时清空两个txt文件
    if os.path.exists("反查失败列表.txt"):
        f = open("反查失败列表.txt", 'w')
        f.truncate()
    if os.path.exists("ip反查结果.txt"):
        f = open("ip反查结果.txt", 'w')
        f.truncate()
    for i in tqdm(url_list):
        catch_result(i)