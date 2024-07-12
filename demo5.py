# 正则表达式
# Regular Expression，正则表达式，一种使用表达式的方式对字符串进行匹配的语法规则
# 正则表达式语言由两种基本字符类型组成：文本字符 和 元字符

# 我们抓取到的网页源代码本质上就是一个超长的字符串，想从里面提取到内容，用正则表达式再合适不过了

# 正则的优点：速度快，效率高，准确性高
# 正则的缺点：新手上手难度有点高

# 不过，只要掌握了正则编写的逻辑关系，写出一个提取页面的正则其实并不复杂

# 正则的语法：使用元字符进行排列组合，用来匹配字符串  在线测试正则表达式 https://www.bejson.com/othertools/regex/

# 元字符：具有特殊意义的专用字符
#  1          .              匹配除换行符以外的任意字符（除了换行符，里面的东西都会匹配出来，一个 . 一个字，两个 . 两个字）
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
# 15       （ ）              匹配括号内的表达式，也表示一个组
# 16        [ . . . ]        匹配字符组中的字符
# 17        [ ^. . . ]       匹配除了字符组中字符的所有字符（需要区分 8，这里的 ^ 含义不一样）
import requests
from bs4 import BeautifulSoup

query = input("请输入一个你喜欢的明星：")
url = f'https://www.sogou.com/web?ie=UTF-8&query={query}'

RequestHeaders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=RequestHeaders)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, "html.parser")

    page_text = soup.get_text()

    clean_text = "\n".join(line.strip() for line in page_text.splitlines() if line.strip())

    with open(f"{query}档案.txt", "w", encoding="utf-8") as f:
        f.write(clean_text)

    print(f"页面文本内容已成功写入到{query}档案.txt文件中。")

else:
    print(f"请求失败，状态码：{resp.status_code}")