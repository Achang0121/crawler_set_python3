# 某某头条的热门新闻抓取

爬虫集合，之前的没做好收集整理，往后都整理到这里。


👀 [某条热门新闻爬虫](https://github.com/Achang0121/crawler_set_python3/tree/ToutiaoNewss)那个由于最近又开始整治了，怕喝茶，所以写了个安全的新闻爬虫，还是那句话，仅仅学习所用。为自己空荡荡的数据库弄点数据。
总的来说，也没啥，抓包分析的参数，有个`_signature`参数是加密的，但是不带这个参数一样可以返回想要的数据。上张图：
![image](https://user-images.githubusercontent.com/40299549/112621437-b5a07e00-8e64-11eb-90d3-8538eedde42b.png)

用motor替换了pymongo；数据重复的问题还是存在。暂时不能访问了，等等再说了。
