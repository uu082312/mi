# for i in range(5, 0, -1):
#     print(i)
# a = list(range(100))[-10:]
# print(a)
# from collections import OrderedDict
# a = dict(OrderedDict(a=1))
# print(a)
# a = OrderedDict()
# a['a'] = 1
# print(a)
# a = ['a', 'b', 'c']
# b = ''.join(a)
# print(b)
# def add(a, b):
#     return a + b
# def fun():
#     for i in range(4):
#         yield i
# g = fun()
# for n in [2, 2]:
#     g = (add(n, i) for i in g)
# print(list(g))
# a = dict([('a', 'b'), (1, 2)])
# print(a)
# k = 1000
# num = 0
# while k >1:
#     num += 1
#     k = k/2
# print(num)
# a =bool({})
# print(a)
# print('ada'> 'vvv')
# print(1<4==4)
# a =1
# def fun(a):
#     a = 2
# fun(a)
# print(a)
# a = r'\'
# print(a)
# a = lambda x, y: x+y
# print(a(1, 2), '---------')
# class p:
#     def __init__(self):
#         pass
#     def fun(self):
#         print(self)
# P = p()
# P.fun()
# from gevent import monkey
# monkey.patch_all()
# import time
# import gevent
# def fun1():
#     print('1')
#     time.sleep(5)
#     print('2')
#
# def fun2():
#     print('3')
#     time.sleep(5)
#     print('4')
#
# g1 = gevent.spawn(fun1)
# g2 = gevent.spawn(fun2)
# g1.join()
# g2.join()
# a = [1, 2]
# b = a
# print(id(a), id(b))
# def fun(a, b):
#     print(id(a), id(b))
#
# a = [1, 2]
# b = [1, 2]
# fun(a, b)
# print(id(a,), id(b))

# import requests
# headres = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# url = 'http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp'
# data = {
# 'TIMEBEGIN_SHOW': '2019-04-04',
# 'TIMEEND_SHOW': '2019-04-13',
# 'TIMEBEGIN': '2019-04-04',
# 'TIMEEND': '2019-04-13',
# 'SOURCE_TYPE': '1',
# 'DEAL_TIME': '02',
# 'DEAL_CLASSIFY': '00',
# 'DEAL_STAGE': '0000',
# 'DEAL_PROVINCE': '0',
# 'DEAL_CITY': '0',
# 'DEAL_PLATFORM': '0',
# 'BID_PLATFORM': '0',
# 'DEAL_TRADE': '0',
# 'isShowAll': '1',
# 'PAGENUMBER': '1',
# 'FINDTXT': '',
# 'validationCode':'',
# }
#
# res = requests.post(url=url, data=data, headers=headres)
# print(type(res.json()))
# def f(a, b, *, c, d):
#     print(a+b+c+d)
#
# f(1, b=2,c=3, d=4)
# def fun(lis=[]):
#     lis.append(0)
#     print(lis)
# lis = []
# fun()
# fun()

# def fun2(s):
#     s += 'a'
#     print(s)
# s = 'heihei'
# fun2(s)
# fun2(s)
# a = dict([('a', 1)])
# print(a)
# a = [1, 2]
# b = ['a', 'b']
# c = zip(a, b)
# print(dict(c))
# class MyException(Exception):
# 	pass
#
#
# try:
#     raise MyException('heihei')
# except MyException as e:
#     print(e)

# def fun(num):
#     nm = str(num)
#     start, end = 0, len(nm)-1
#     while start < end//2:
#         if nm[start] == nm[end]:
#             start += 1
#             end -= 1
#         else:
#             return '不是回文串'
#     return '是回文串'
# print(fun(12321098))
# from functools import reduce
# ret = reduce(lambda x, y: x+y, range(101))
# print(ret)
# a = ['a', 'b']
# b = [1, 2]
# c = zip(a, b)
# print(dict(c))
# a = [{'name': 'bb', 'age': 20}, {'name': 'aa','age': 18}]
# b = sorted(a, key=lambda x: x['age'], reverse=True)
# print(b)


class F:
    def __enter__(self):
        print('进来了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('出来了')

    def run(self):
        print('调用了')

with F() as a:
    a.run()
    # int("aaa")

