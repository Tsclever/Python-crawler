# 项目5 正则表达式和re模块的使用
# 项目介绍：这也称不上项目，只能算是正则表达式和re库的练习
# 注意：写好爬虫，正则表达式是必不可少的，要好好学！！！

# 正则表达式
# Regular Expression，正则表达式，一种使用表达式的方式对字符串进行匹配的语法规则
# 正则表达式语言由两种基本字符类型组成：文本字符 和 元字符

# 我们抓取到的网页源代码本质上就是一个超长的字符串，想从里面提取到内容，用正则表达式再合适不过了

# 正则的优点：速度快，效率高，准确性高
# 正则的缺点：新手上手难度有点高

# 不过，只要掌握了正则编写的逻辑关系，写出一个提取页面的正则其实并不复杂

# 正则的语法：使用元字符进行排列组合，用来匹配字符串  在线测试正则表达式 https://www.bejson.com/othertools/regex/

# 元字符：具有特殊意义的专用字符
#  1         .              匹配除换行符以外的任意字符（除了换行符，里面的东西都会匹配出来，一个 . 一个字，两个 . 两个字）
#  2        \w               匹配字母，数字，下划线
#  3        \s               匹配任意的空白符（空格）
#  4        \d               匹配数字
#  5        \n               匹配一个换行符
#  6        \t               匹配一个制表符
#  7
#  8         ^               匹配字符串的开始
#  9         $               匹配字符串的结尾
# 10
# 11        \W               匹配 非 字母或数字或下划线
# 12        \D               匹配 非 数字
# 13        \S               匹配 非 空白符
# 14        a|b              匹配 字符a 或者 字符b（只能显示 a 或 b）
# 15        ( )              匹配括号内的表达式，也表示一个组
# 16        [ . . . ]        匹配字符组中的字符
# 17        [ ^. . . ]       匹配除了字符组中字符的所有字符（需要区分 8，这里的 ^ 含义不一样）

# 量词：控制前面的元字符出现的次数
#  1         *              重复 零次 或 更多次（以\d*为例：零次：匹配失败显示为空，更多次：匹配成功显示为一段长数字）
#  2         +              重复 一次 或 更多次（以\d+为例：一次：只有一个数字，更多次：有一长串数字，有数字就会成功
#  3         ?              重复 零次 或 一次   （以\d?为例：零次：匹配失败显示为空，一次：匹配成功只显示一个数字）
#  4        {n}             重复 n 次（\d\d\d\d\d = \d{5}）
#  5        {n,}            重复 n 次或 更多次（ \d{1,} 意思是从第1位到最后）
#  6        {n,m}           重复 n 到 m 次（ \d{1,1} 意思是从第1位到第一位，\d{5} = \d{1,5}）

# 贪婪匹配和惰性匹配
#  1         .*             贪婪匹配（全部匹配）
#  2         .*?            惰性匹配（精确匹配）

# 这两个很重要，因为我们写爬虫用的最多的就是这个惰性匹配
# 所以我们能发现一个规律：.? 表示尽可能少的匹配，. 表示尽可能多的匹配，暂时先记住这个规律，后面写爬虫会用到


# Python 自带的标准库中包含了 re 模块
import re

# findall(): 字符串中所有的符合正则的内容（效率不高，网页内容很多很长）
list1 = re.findall("m", "maybe you are a mm, mai yi mai")
print(list1)   # ['m', 'm', 'm', 'm', 'm']

# \d 匹配数字   + 重复一次或更多次   \d+ 匹配里面的所有数字
list1 = re.findall(r"\d+", "我的电话是：10086，我女盆友的电话是：10010")
print(list1)   # ['10086', '10010']


# finditer: 匹配字符串中所有的内容(返回的是迭代器), 从迭代器中拿到内容需要 .group() 方法
list2 = re.finditer(r"\d+", "我的电话是：10086")
# print(list2)   <callable_iterator object at 0x7fd9c533bb50>   这里说明了list2是 迭代器

for i in list2:
# print(i)   <re.Match object; span=(6, 11), match='10086'>   正则表达式; 字符串从索引 6 开始，到索引 11 结束, 匹配到的字符串是 10086
  print(i.group())   # 10086


# search, 找到一个结果就返回, 返回的结果是match对象, 如果匹配不上，search返回的结果是none, 拿数据需要 .group()
list3 = re.search(r"\d+", "我的电话是：10086，我女盆友的电话是：10010")
print(list3.group())   # 输出10086


# match 是从头开始匹配, 条件是 \d+ , 只匹配纯数字, 类似于 ^\d+
list4 = re.match(r"\d+", "我的电话是：10086，我女盆友的电话是：10010")
print(list4.group())   # 'NoneType' object has no attribute 'group'   list4 为空

list4 = re.match(r"\d+", "10086，我女盆友的电话是：10010")
print(list4.group())   # 10086


# 预加载正则表达式     提前加载，提高效率
obj = re.compile(r"\d+")   # 将正则表达式编译成一个 正则表达式对象，规则为匹配所有数字

list5 = obj.finditer("我的电话是: 10086")   # 正则表达式调用 finditer
for i in list5:
  print(i.group())   #10086

list5 = obj.findall("替换成: 1001001001")   # 正则表达式调用 findall
for i in list5:
  print(i)   # 1001001001


s = """""
<div class='zjl'><span id='1'>周杰伦</span></div>
<div class='jjj'><span id='2'>林俊杰</span></div>
<div class='xzq'><span id='3'>薛之谦</span></div>
<div class='cyl'><span id='4'>蔡依林</span></div>
<div class='jjs'><span id='5'>界沮授</span></div>
"""

# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)  # re.S  让 . 能匹配换行符

result = obj.finditer(s)
for i in result:
  print(i.group())        # <div class='zjl'><span id='1'>周杰伦</span></div>
  print(i.group("id"))    # 获取id组的内容，输出：1
  print(i.group("name"))  # 获取name组的内容，输出：周杰伦