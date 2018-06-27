dongfang说明文档
==
介绍
 - 
dongfang是一个基于Scrapy-Selenium的股票信息爬虫，爬取了东方网千股千评的所有股票信息。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Selenium 3.11.0
* Faker(随机切换User-Agent)<br>

### 其它
爬取东方网千股千评的时候，其个股信息采用了AJAX加载方式，然后分析其动态加载链接的规律，发现其动态链接返回的看似是一个JSON格式的文件，实际过程中无法用json.loads()获得其数据。试着用正则表达式获取其中的信息，也获取成功了，就是代码看着很复杂，遂采用selenium来获取。抓取过程中基本没有问题，而且对于这种获取数据量不大的情况下，selenium的速度慢影响不大。

爬取结果
-
在东方财富网的千股千评页面总共获取了3659条个股信息。每条信息中还包括了该股票的个股研报和其股吧的链接。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图:<br>
![股票信息截图](https://github.com/lanluyu/dongfang/blob/master/stocks.PNG)
