import requests
import os

def main():
    url = 'https://ip.164746.xyz/ipTop.html'
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            ip_domin = []
            for ip in resp.text.split('\n'):
                # 去除可能的空格和换行符
                ip = ip.strip()
                if ip:
                    ip_domin.append(ip + '.example.com')
            # 写入文件 README.md
            with open(os.path.join(os.getcwd(), 'README.md'), 'w') as f:
                for ip in ip_domin:
                    f.write(ip + '\n')
        else:
            print(f"Request failed with status code: {resp.status_code}")
    except requests.RequestException as e:
        print(f"Error occurred during request: {e}")
    except IOError as e:
        print(f"Error occurred during file write: {e}")
    # 写入文件 README.md
    with open(os.path.join(os.getcwd(), 'README.md'), 'w') as f:
        f.write("# IP Addresses with example.com\n")
        for ip in ip_domin:
            f.write(f"- {ip}\n")

if __name__ == "__main__":
    main()