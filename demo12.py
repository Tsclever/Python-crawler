# 项目12 xpath解析入门-2

from lxml import etree

tree = etree.parse("demo12.html")
result1 = tree.xpath('/html')
result2 = tree.xpath("/html/body/ul/li[1]/a/text()")   # xpath的顺数是从1开始数的, []表示索引
result3 = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")   # [@xxx=xxx] 属性的筛选
# print(result)

ol_li_list = tree.xpath("/html/body/ol/li")
for i in ol_li_list:
  # 从每一个li中提取到文字信息
  result = i.xpath("./a/text()")   # 在当前li标签中继续去寻找, ./ 相对查找
  print(result)
  result2 = i.xpath("./a/@href")   # 没有[], 就是确切的属性值
  print(result2)

print(tree.xpath("/html/body/ul/li/a/@href"))   # ['http://www.baidu.com/', 'http://www.google.com/', 'http://www.sogou.com/']

# 通过google浏览器, 右键查看代码, 打开菜单栏, 可以复制xpath路径
print(tree.xpath("/html/body/div[1]/text()"))
print(tree.xpath("/html/body/ol/li[2]/a"))