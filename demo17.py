# 项目17 爬取网易云热评
# 项目介绍：1.找到未加密的参数                       window.arsrss(参数, xxx, xxx)
#          2.想办法把参数进行加密(必须参考网易的逻辑), parms => encText , encSeckey => encSecKey
#          3.发送请求给网易，拿到评论信息

import requests
from Crypto.Cipher import AES   # 这里要注意, pycrypto库已经不再维护, 所以需要安装pycryptodome库, pip3 install --upgrade pycryptodome
from base64 import b64encode
import json

# post请求
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data = {
  "csrf_toke":"",
  "cursor":"-1",
  "offset":"0",
  "orderType":"1",
  "pageNo":"1",
  "pageSize":"20",
  "rid":"R_SO_4_1397345903",
  "threadId":"R_SO_4_1397345903",
}

# 服务于window.a
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "aoXPEepbtmAXgScB"   # 手动固定的  ->  人家函数中是随机的

def get_encSecKey():     # 由于i是固定的, 那么encSecText就是固定, c()函数的结果就是固定的
  return "667a1904992a40ed682ac07f48ae2485145355295493213350a870b04ed1b9584bf51f93242519eb4ce272b13380ec8dad52f8b893a3d7d162538a14008089e5fe49ac85d610f6606899d2fdcf1f367f50264063e7ad0de18abf671b342910079b71fe6af21113b58500929d089f5138c631a7d5f300fcba5c469ade93ae7b7b"

# 把参数进行加密
def get_params(data):   # 默认这里接收到的是字符串
  first = enc_params(data, g)
  second = enc_params(first, i)
  return second   # 返回的是params

# 转换成16的倍数, 位下方的加密算法服务
def to_16(data):
  pad = 16 - len(data) % 16
  data += chr(pad) * pad
  return data

# 加密过程
def enc_params(data, key):   
  iv = "0102030405060708"
  data = to_16(data)
  aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)   # 创建加密器
  bs = aes.encrypt(data.encode("utf-8"))   # 加密, 加密的内容的长度必须是16的倍数, ""
  return str(b64encode(bs), "utf-8")   # 转化成字符串返回



# 处理加密过程
"""
    function a(a) {   # 随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)   # 循环16细次
            e = Math.random() * b.length,   # 随机数
            e = Math.floor(e),   # 取整
            c += b.charAt(e);    # 取字符串中的xxx位置
        return c
    }
    function b(a, b) {   # a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b)   # b 密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)   # e 数据
          , f = CryptoJS.AES.encrypt(e, c, {   # AES是加密方法, c是加密的密钥
            iv: d,   # 偏移量
            mode: CryptoJS.mode.CBC   # 模式: cbc
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d: 数据,  e: 010001,  f: 00e0b5....,  g: 0CoJUm6Qyw8W8jud
        var h = {}   # 空对象
          , i = a(16);   # i就是一个16位的随机值
        return h.encText = b(d, g),   # g 密钥
        h.encText = b(h.encText, i),   # 返回的就是params, i也是密钥
        h.encSecKey = c(i, e, f),   # 返回的就是encSecKey, e和f是定死的, 如果此时我把i的值固定, 得到的key一定是固定的
        h
    }

    两次加密: 
    数据+g -> b -> 第一次加密+i -> b = params
"""

# 发送请求, 得到评论
resp = requests.post(url, data={
  "params": get_params(json.dumps(data)),
  "encSecKey": get_encSecKey()
})

# print(resp.text)

# 解析 JSON 数据
response_text = resp.text
parsed_data = json.loads(response_text)

# 提取评论数据
comments = parsed_data['data']['comments']

# 打印评论内容
for comment in comments:
    user_info = comment['user']
    content = comment['content']
    rich_content = comment['richContent']
    
    print("用户昵称:", user_info['nickname'])
    print("评论内容:")
    print(content)
    print("\n富文本内容:")
    print(rich_content)
    print("时间:", comment['timeStr'])
    print("-" * 40)
