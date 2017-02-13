# 笔记本推荐
## 背景
本人苦逼软件工程师一枚，经常有亲戚好友让我推荐购买的笔记本电脑。然鹅本人对硬件不太了解，就想了一个偷懒的办法，如下：  

从[ZOL网站](http://www.zol.com.cn/)上根据条件过滤出一堆笔记本的信息，先根据CPU优劣进行排行，然后再根据GPU优劣进行排行，得出一个笔记本的总排行榜，选择几个排行靠前的向亲戚好友推荐。

### 启动类
[启动类](src/main.py)
### 主要的参数
. pageSize = 15;#获取ZOL笔记本列表的总页数	
. _menuId = 223;#笔记本的品牌Id，联想：160，惠普：223，苹果：544，	
. _minprice = 3000;#笔记本的最低价格	
. _maxprice = 4000;#笔记本的最高价格	

### CPU,GPU优劣
CPU和GPU的优劣是根据CPU和GPU的排行榜得出。	
当前项目的CPU，GPU的排行榜信息时保存在cpurank.txt，gpurank.txt文件中，该排行榜数据是从
[GPU排行榜](http://itianti.sinaapp.com/index.php/mgpu),[CPU排行榜](http://itianti.sinaapp.com/index.php/mcpu)处获取。

