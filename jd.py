import requests
from lxml import etree
# import URLEncoder
# a = URLEncoder.encode('华为', "utf-8")
# print(a)
# a = '华为'

# print(a)
url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAp30pro&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E5%8D' \
      '%8E%E4%B8%BAp30pro&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&page=5&s=112&click=0'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


res = requests.get(url=url, headers=headers)
ret = res.content.decode('utf-8')
tree = etree.HTML(ret)
ret = tree.xpath('//div[@id="J_main"]//ul/li//span/a/text()')
pag = tree.xpath('//div[@id="J_bottomPage"]//text()')
print(ret)
print(pag)
print(res.url)