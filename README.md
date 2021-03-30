# 某某头条的热门新闻抓取


👀 [某条热门新闻爬虫](https://github.com/Achang0121/crawler_set_python3/tree/ToutiaoNewss)
那个由于最近又开始整治了，怕喝茶，所以写了个安全的新闻爬虫，还是那句话，仅仅学习所用。为自己空荡荡的数据库弄点数据。

> 网页分析

上张图，内容加载的网络请求如下：
![image](https://user-images.githubusercontent.com/40299549/112621437-b5a07e00-8e64-11eb-90d3-8538eedde42b.png)

动态参数：

- `max_behot_time`：是时间戳
- `_signature`： 不带该参数能正常返回

问题：

- 由于请求的url中对该次请求返回的数据量没有体现。每次请求只改动`max_behot_time`，数据会有重复，而且一直重复。很快爬虫就会停了。
- 请求频率得克制点，不然返回都是空。


---
