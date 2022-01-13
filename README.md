# DomainSpiderSE
     一款基于国内两大SEO搜索引擎爱站和站长之家的子域名爬取工具。
     
### 环境
  安装依赖：
  
     pip install -r requirement.txt
     
  使用selenium模块依赖chromedriver，根据自己Chrome版本下载对应版本。
  
  chromedriver国内镜像下载地址：http://npm.taobao.org/mirrors/chromedriver/
  
  下载完后解压，将chromedriver.exe文件复制到Chrome的Google/Chrome/Application目录下和Python的安装目录。
 
### 用法
python spiderSE.py -h

    ************************************************************
            github：https://github.com/ltfafei
              CSDN: afei00123.blog.csdn.net
                   公众号：网络运维渗透

    ************************************************************

    usage: spiderSE.py [-h] -d URL -f FILES [--option {a,z}]

    SearchEngine domain spider Script

    optional arguments:
      -h, --help            show this help message and exit
      -d URL, --url URL     please input master domain. eg: xxx.com
      -f FILES, --files FILES
                            Please input url_file path to save. eg: c:\urls.txt
      --option {a,z}        --option a：使用爱站爬虫；--option z：使用站长之家爬虫（默认使用站长之家爬虫）


python spiderSE.py -d xxx.cn -f urls.txt

![image](https://user-images.githubusercontent.com/43526141/119491345-62797780-bd90-11eb-9360-3609256fc37e.png)


python spiderSE.py -d xxx.edu.cn -f urls1.txt --option a

![image](https://user-images.githubusercontent.com/43526141/119490973-00b90d80-bd90-11eb-9091-702b7967afd5.png)



