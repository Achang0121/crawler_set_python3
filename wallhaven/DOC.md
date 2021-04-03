> [wallhaven](https://wallhaven.cc/) 某图片网站，资源极其丰富

---

> 实现登陆流程

1. 抓包发现，POST请求的参数只有三个 `_token`、`username`、`password`
2. 全局搜索 `_token` 和它的值，意外发现 `_token`的值和登陆页面中的```<meta name="csrf-token" content="">``` content值是一样的。
3. 发两次请求，第一次GET获取`_token`；第二次POST带着获得的`_token`和账号密码，发送请求。
4. 啧啧，👌，顺利返回登陆成功的个人页面。🚬

---
测试的结果在[这里](https://github.com/Achang0121/crawler_set_python3/blob/main/wallhaven/wallhaven/login/tmp.html)

> 这个网站的url非常有意思

`https://wallhaven.cc/search?categories=111&purity=001&topRange=1M&sorting=toplist&order=desc&page=2`

要说的是2个参数：
- categories : [General, Amine, People]
- purity : [SFW, Sketchy, NSFW]

  长度固定为3位，每一位的值是1 or 0；
  对应页面的两个过滤标签，可多选，1代表选中；
  
不说了，这个网站挺有意思。
要测试的各位得自己修改账号密码了，先这么地了。和谐社会和谐社会

🔞不保证所有的图片都符合和谐社会都要求，各位慎重。

---
