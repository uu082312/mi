import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '73.0.3683.86 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://m.ctrip.com/html5/flight/swift/domestic/BJS/SHA/2019-05-04?allianceid=4897&sid=155947&ouid=cuop',
    'Content-Type': 'application/json',
    'Origin': 'https://m.ctrip.com'

}
# data = {
# '_fxpcqlniredt': '09031168110020610302'
# }
data1 = {"preprdid": "", "trptpe": 1, "flag": 8,
         "searchitem": [{"dccode": "BJS", "accode": "SHA", "dtime": "2019-05-04"}],
         "contentType": "json", "flag": 8, "head": {"cid": "09031168110020610302", "ctok": "", "cver": "1.0",
                                                    "lang": "01", "sid": "8888", "syscode": "09", "auth": "null",
                                                    "cid": "09031168110020610302", "ctok": "",
                                                    "cver": "1.0", "extension": [{"name": "aid", "value": "4897"},
                                                                                 {"name": "sid", "value": "155947"},
                                                                                 {"name": "protocal",
                                                                                  "value": "https"}],
                                                    0: {"name": "aid", "value": "4897"},
                                                    1: {"name": "sid", "value": "155947"},
                                                    2: {"name": "protocal", "value": "https"},
                                                    "lang": "01", "sid": "8888", "syscode": "09", "preprdid": "",
                                                    "searchitem": [
                                                        {"dccode": "BJS", "accode": "SHA", "dtime": "2019-05-04"}],
                                                    0: {"dccode": "BJS", "accode": "SHA", "dtime": "2019-05-04"},
                                                    "accode": "SHA",
                                                    "dccode": "BJS",
                                                    "dtime": "2019-05-04",
                                                    "subchannel": "null",
                                                    "tid": "{4c333ac2-1929-49d9-b205-c82de0f741a5}",
                                                    "trptpe": 1
                                                    }}

url = 'https://m.ctrip.com/restapi/soa2/14022/flightListSearch?_fxpcqlniredt=09031168110020610302'
ret = requests.post(url=url, data=data1, headers=headers)
print(ret.text)
