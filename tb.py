import requests
import re
import time

url = 'https://s.taobao.com/search?q=%E7%94%B7%E8%A3%85'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'cookie': 'miid=180252421502287677; thw=cn; t=9a89fe09ff93fcc9fe29a54678ac43da; cna=aJREFN8YuDYCAd9IY0+WxsPB; ' \
              'hng=CN%7Czh-CN%7CCNY%7C156; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; enc=4ohMSzLNtBtO2uzEi%2FO9vw9al26%2FQMfZ%2FBLbHae' \
              'TPbeXYkjTH1SV1pceLfYCd3d9PFuQLRtSe3PCpWuw06tiIg%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3' \
              'D0%26__ll%3D-1%26_ato%3D0; mt=ci=0_0; v=0; cookie2=1e4de7572a09f4c2bfc0dd0ad74d0487; _tb_token_=e6113eee3337' \
              '3; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=8D6BBB8E7740A477D486CF507995B961; ' \
              'l=bBOJ8S0rvA8dJ4V2BOCgZuIJ1O7tSIRAguPRwGVXi_5ZJ6L6FRbOlQ1OqFp6Vj5R6ELB4Q6MVtp9-etki; isg=BB4epM7nzozpORq63eb' \
              'HVBNfb7Sgd-0wzP1EQsingGFc677FMG7laf2J57fCU9px'

}

res = requests.get(url=url, headers=headers)
ret = res.content.decode('utf-8')
print(ret)
with open('./tb.html', 'w', encoding='utf-8') as f:
    f.write(ret)
# result = re.findall(r'.*?(?P<title>"title":".*?,").*'
#           r'(?P<view_sales>"view_sales":".*?",")', ret)
# print(result)
# r = "".join(result)
# with open('./tb.txt', 'a', encoding='utf-8') as f:
#     f.write(str(result))
# print(ret)
