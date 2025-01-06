import requests
url = 'https://ip.164746.xyz/ipTop.html'
resp = requests.get(url)
ip_domin = []
# 每个IP 对应一个 example.com
for ip in resp.text.split('\n'):
    ip_domin.append(ip + ' example.com')
# 写入文件 README.md
with open('README.md', 'w') as f:
    for ip in ip_domin:
        f.write(ip + '\n')