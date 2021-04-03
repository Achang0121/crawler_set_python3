import json
import re
import requests


headers = {
    'referer': 'https://wallhaven.cc/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

url_of_login_web = 'https://wallhaven.cc/login/'
url_of_login_request = 'https://wallhaven.cc/auth/login'

session = requests.session()

login_html_text = session.get(
    url=url_of_login_web, headers=headers, verify=False).text

token = re.findall(
    r'<meta name="csrf-token" content="(.*?)">', login_html_text)[0]

data = {
    "_token": token,
    "username": "username", # 登陆账号
    "password": "password" # 自己账号的密码，没错，这个网站明文传输密码
}

headers['referer'] = url_of_login_web

response = session.post(url=url_of_login_request,
                        data=data, headers=headers, verify=False)

cookies = requests.utils.dict_from_cookiejar(response.cookies)


"""
=========以下部分，未成年的朋友请慎重离开。=========

成功登陆后，顺利获取到cookies

再次抓取都内容质量和丰富程度就和登陆之前完全不一样了

以下是小测一把

"""
pics_html = session.get(
    url='https://wallhaven.cc/search?categories=111&purity=001&topRange=1M&sorting=toplist&order=desc&page=2',
    cookies=cookies,
    headers=headers,
    verify=False
).text

# 提取规则自己写了，暂时不想弄了，那个tmp.html文件是测试访问得到的结果，是登陆状态，而且，未成年不要看
REGEX = re.compile('<a class="preview" href="(.*?)"')
links = REGEX.findall(pics_html)
print(links)
