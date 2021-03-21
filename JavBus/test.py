import requests
import random

headers = {
    'Host': 'www.javbus.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Refer': 'https://www.javbus.com/SSIS-013',
}

gid = '45864938377'
lang = 'zh'
img = 'https://pics.javbus.com/cover/853n_b.jpg'
uc = '0'

url = f"https://www.javbus.com/ajax/uncledatoolsbyajax.php?gid={gid}&lang={lang}&img={img}&uc={uc}&floor={int(random.random() * 1000) + 1}"

proxy = {
    'http': 'http://192.168.1.8:7890',
    'https': 'https://192.168.1.8:7890',
}

response = requests.get(url, proxies=proxy, verify=False)
if response.status_code == 200:
    print(response.text)
