# 项目11 xpath解析入门-1

from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">界徐盛</nick>
        <nick id="10010">界沮授</nick>
        <nick class="zjl">周杰伦</nick>
        <nick class="ljj">林俊杰</nick>
        <div>
            <nick>发大财1</nick>
        </div>
        <span>
            <nick>发大财2</nick>
        </span>
    </author>

    <partner>
        <nick id="xb">小白</nick>
        <nick id="xh">小黑</nick>
    </partner>
</book>
"""

# Element 节点
tree = etree.XML(xml)
# result = tree.xpath("/book")   # /表示层级关系，第一个 / 是节点    [<Element book at 0x7f02ceb33200>]
# result = tree.xpath("/book/name")   # book节点里的name节点
# result = tree.xpath("/book/name/text()")   # text()拿文本   ['野花遍地香']
# result = tree.xpath("/book/author//nick/text()")   # 拿出/author里所有的nick(子孙后代)
# result = tree.xpath("/book/*/nick/text()")   #  * 通配符, 任意的一个节点
result = tree.xpath("/book//nick/text()")   # 拿出/book里有的nick标签里的内容


print(result)