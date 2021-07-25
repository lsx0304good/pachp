from lxml import etree

data = '''
<!DOCTYPE html>
<html lang="en">
　　<head>
　　　　<meta charset="UTF-8" />
　　　　<title>测试页面</title>
</head>
<body>
　　<ol class="firstol">
　　　　<li class="haha">醉卧沙场君莫笑，古来征战几人回</li>
　　　　<li class="heihei">两岸猿声啼不住，轻舟已过万重山</li>
　　　　<li id="hehe" class="haha">一骑红尘妃子笑，无人知是荔枝来</li>
　　　　<li class="xixi">停车坐爱枫林晚，霜叶红于二月花</li>
　　　　<li class="lala">商女不知亡国恨，隔江犹唱后庭花</li>
　　</ol>
　　<div id="pp">
　　　　<div>
　　　　　　<a href="http://www.baidu.com">李白</a>
　　　　</div>
　　　　<ol>
　　　　　　<li class="huanghe">君不见黄河之水天上来，奔流到海不复回</li>
　　　　　　<li id="tata" class="hehe">李白乘舟将欲行，忽闻岸上踏歌声</li>
　　　　　　<li class="tanshui">桃花潭水深千尺，不及汪伦送我情</li>
　　　　</ol>
　　　　<div class="hh">
　　　　　　<a href="http://mi.com">雷军</a>
　　　　</div>
　　　　<div class="kk">
　　　　　　<b href="http://mi.com"><c>3</c></b>
　　　　　　<b href="http://mi.com"><c>5</c></b>
　　　　　　<b href="http://mi.com"><c>6</c></b>
　　　　　　<b href="http://mi.com"><c>8</c></b>
　　　　　　<b href="http://mi.com"><c>9</c></b>
　　　　　　<b href="http://mi.com"><c>3</c></b>
　　　　</div>
　　　　<ol class="lastol">
　　　　　　<li class="dudu">are you ok</li>
　　　　　　<li class="meme">会飞的猪</li>
　　　　</ol>
　　</div>
</body>
</html>
'''

html_etree = etree.HTML(data)  # <Element html at 0x7faf44ed5140>

# get all <a> tags
a = html_etree.xpath("//a")

# get all li tags named 'haha' and get text
li = html_etree.xpath("//li[@class='haha']/text()")
# print(li)

# get all li tags contain 'haha' and get text
li1 = html_etree.xpath("//li[contains(@class,'haha')]/text()")
# print(li1)

# not contain
li2 = html_etree.xpath("//li[not(contains(@class,'haha'))]/text()")

ol_ele = html_etree.xpath("//ol[@class='lastol']")[0]
oli1 = ol_ele.xpath("//li/text()")  # 查询的还是全局, 等同于 html_etree.xpath
# print(oli1)
oli2 = ol_ele.xpath(".//li/text()")  # 查询的是当前分支
# print(oli2)
#
# for li in oli1:
#     print(li)


ol = html_etree.xpath("//ol[@class='firstol']")[0]
# lis = ol.xpath(".//li[1]/text()")
# lis = ol.xpath(".//li[last()]/text()")
# lis = ol.xpath(".//li[last()-1]/text()")
# lis = ol.xpath(".//li[position()>3]/text()")
# print(lis)


div = html_etree.xpath("//div[@class='kk']")[0]
print(div.xpath(".//@*"))