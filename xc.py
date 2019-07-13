import json


data = """{
	"ResponseStatus": {
		"Timestamp": "/Date(1556866882881+0800)/",
		"Ack": "Success",
		"Errors": [],
		"Build": null,
		"Version": null,
		"Extension": [{
			"Id": "CLOGGING_TRACE_ID",
			"Version": null,
			"ContentType": null,
			"Value": "7106397626379416755"
		}, {
			"Id": "RootMessageId",
			"Version": null,
			"ContentType": null,
			"Value": "921812-0a08ac8f-432463-61150"
		}]
	},
	"fltitem": [{
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1831",
				"ishared": false
			},
			"craftinfo": {
				"craft": "359",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 07:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 09:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "97",
				"mtip": "准点率高",
				"info": "97"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 520,
				"drate": 0.35,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥208起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "L",
				"drate": 0.35,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODMxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥75起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODMxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1835",
				"ishared": false
			},
			"craftinfo": {
				"craft": "333",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 08:05:00",
				"dweek": "周六",
				"adate": "2019-05-04 10:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "90",
				"mtip": "准点率高",
				"info": "90"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 520,
				"drate": 0.35,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥208起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "L",
				"drate": 0.35,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODM1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjA1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥75起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODM1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjA1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1519",
				"ishared": false
			},
			"craftinfo": {
				"craft": "359",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 09:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 11:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "90",
				"mtip": "准点率高",
				"info": "90"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 520,
				"drate": 0.35,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥208起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "L",
				"drate": 0.35,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTE5IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA5OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 5
			}],
			"classinfor": [{
				"rmktitle": "退改¥75起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTE5IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA5OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "NAY",
				"aportsname": "南苑",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "KN",
				"airsname": "中联航",
				"flgno": "KN5737",
				"ishared": false
			},
			"craftinfo": {
				"craft": "73V",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 07:50:00",
				"dweek": "周六",
				"adate": "2019-05-04 09:50:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "97",
				"mtip": "准点率高",
				"info": "97"
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 538,
				"drate": 0.4,
				"ticket": 6
			}],
			"classinfor": [{
				"rmktitle": "退改¥323起",
				"ifb": "无托运行李额",
				"cgrd": 0,
				"sclass": "V",
				"drate": 0.4,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiS041NzM3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjUwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "HO",
				"airsname": "吉祥",
				"flgno": "HO1252",
				"ishared": false
			},
			"craftinfo": {
				"craft": "321",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 06:50:00",
				"dweek": "周六",
				"adate": "2019-05-04 09:05:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "67",
				"mtip": "准点率较高",
				"info": "67"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均8分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 650,
				"drate": 0.48,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥325起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "W",
				"drate": 0.48,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSE8xMjUyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA2OjUwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1100,
				"drate": 0.54,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥220起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.54,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSE8xMjUyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA2OjUwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1531",
				"ishared": false
			},
			"craftinfo": {
				"craft": "32A",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 10:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 12:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "83",
				"mtip": "准点率高",
				"info": "83"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 660,
				"drate": 0.45,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥198起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "S1",
				"drate": 0.45,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTMxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEwOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 4
			}],
			"classinfor": [{
				"rmktitle": "退改¥75起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTMxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEwOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T1",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5183",
				"ishared": false
			},
			"craftinfo": {
				"craft": "325",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 07:35:00",
				"dweek": "周六",
				"adate": "2019-05-04 09:50:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "90",
				"mtip": "准点率高",
				"info": "90"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 670,
				"drate": 0.45,
				"ticket": 6
			}],
			"classinfor": [{
				"rmktitle": "退改¥335起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "S",
				"drate": 0.45,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTgzIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjM1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1500,
				"drate": 0.27,
				"ticket": 8
			}],
			"classinfor": [{
				"rmktitle": "退改¥300起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTgzIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjM1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "NAY",
				"aportsname": "南苑",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T1",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "KN",
				"airsname": "中联航",
				"flgno": "KN5977",
				"ishared": false
			},
			"craftinfo": {
				"craft": "73V",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 11:55:00",
				"dweek": "周六",
				"adate": "2019-05-04 14:05:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "80",
				"mtip": "准点率高",
				"info": "80"
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 678,
				"drate": 0.5,
				"ticket": 5
			}],
			"classinfor": [{
				"rmktitle": "退改¥339起",
				"ifb": "无托运行李额",
				"cgrd": 0,
				"sclass": "R",
				"drate": 0.5,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiS041OTc3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDExOjU1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T1",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "HU",
				"airsname": "海航",
				"flgno": "HU7611",
				"ishared": false
			},
			"craftinfo": {
				"craft": "787",
				"kind": "大",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 07:40:00",
				"dweek": "周六",
				"adate": "2019-05-04 09:55:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "93",
				"mtip": "准点率高",
				"info": "93"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均8分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 710,
				"drate": 0.48,
				"ticket": 7
			}],
			"classinfor": [{
				"rmktitle": "退改¥213起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "V",
				"drate": 0.48,
				"display": "经典经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjExIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjQwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1320,
				"drate": 0.24,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥264起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.24,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjExIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjQwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU4682",
				"ishared": true,
				"sharedflgno": "HO1252",
				"sharedairsname": "吉祥"
			},
			"craftinfo": {
				"craft": "321",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 06:50:00",
				"dweek": "周六",
				"adate": "2019-05-04 09:05:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "67",
				"mtip": "准点率较高",
				"info": "67"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 730,
				"drate": 0.54,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥365起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "R",
				"drate": 0.54,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU0NjgyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA2OjUwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T1",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "HU",
				"airsname": "海航",
				"flgno": "HU7607",
				"ishared": false
			},
			"craftinfo": {
				"craft": "351",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 08:45:00",
				"dweek": "周六",
				"adate": "2019-05-04 11:00:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "93",
				"mtip": "准点率高",
				"info": "93"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均8分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 790,
				"drate": 0.54,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥237起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "X",
				"drate": 0.54,
				"display": "经典经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjA3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjQ1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1400,
				"drate": 0.25,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥280起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.25,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjA3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjQ1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "NAY",
				"aportsname": "南苑",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T1",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "KN",
				"airsname": "中联航",
				"flgno": "KN5987",
				"ishared": false
			},
			"craftinfo": {
				"craft": "73V",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 19:20:00",
				"dweek": "周六",
				"adate": "2019-05-04 21:30:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "50",
				"mtip": "准点率较高",
				"info": "50"
			}, {
				"type": 5,
				"tip": "出票较慢，保证100%出票",
				"stip": null,
				"mtip": "保证出票",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 818,
				"drate": 0.61,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥328起",
				"ifb": "无托运行李额",
				"cgrd": 0,
				"sclass": "T",
				"drate": 0.61,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiS041OTg3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE5OjIwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5160",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 21:50:00",
				"dweek": "周六",
				"adate": "2019-05-04 23:55:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 830,
				"drate": 0.56,
				"ticket": 8
			}],
			"classinfor": [{
				"rmktitle": "退改¥415起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "R",
				"drate": 0.56,
				"display": "经济舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNVTUxNjAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMjE6NTA6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}, {
			"priceinfo": [{
				"price": 1800,
				"drate": 0.32,
				"ticket": 6
			}],
			"classinfor": [{
				"rmktitle": "退改¥360起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNVTUxNjAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMjE6NTA6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5156",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 08:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 10:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "57",
				"mtip": "准点率较高",
				"info": "57"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 830,
				"drate": 0.56,
				"ticket": 7
			}],
			"classinfor": [{
				"rmktitle": "退改¥415起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "R",
				"drate": 0.56,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTU2IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥298起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTU2IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5102",
				"ishared": false
			},
			"craftinfo": {
				"craft": "333",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 08:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 10:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "93",
				"mtip": "准点率高",
				"info": "93"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 830,
				"drate": 0.56,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥415起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "R",
				"drate": 0.56,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTAyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥298起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTAyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5104",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 09:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 11:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "87",
				"mtip": "准点率高",
				"info": "87"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 830,
				"drate": 0.56,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥415起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "R",
				"drate": 0.56,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTA0IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA5OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 6
			}],
			"classinfor": [{
				"rmktitle": "退改¥298起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTA0IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA5OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1883",
				"ishared": false
			},
			"craftinfo": {
				"craft": "332",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 20:20:00",
				"dweek": "周六",
				"adate": "2019-05-04 22:35:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "73",
				"mtip": "准点率较高",
				"info": "73"
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 830,
				"drate": 0.56,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥249起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "W",
				"drate": 0.56,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODgzIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjIwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1790,
				"drate": 0.32,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥90起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODgzIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjIwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5128",
				"ishared": false
			},
			"craftinfo": {
				"craft": "773",
				"kind": "大",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 21:05:00",
				"dweek": "周六",
				"adate": "2019-05-04 23:20:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "55",
				"mtip": "准点率较高",
				"info": "55"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 830,
				"drate": 0.56,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥415起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "R",
				"drate": 0.56,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTI4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIxOjA1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1800,
				"drate": 0.32,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥360起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTI4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIxOjA1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MF",
				"airsname": "厦航",
				"flgno": "MF3020",
				"ishared": true,
				"sharedflgno": "MU5160",
				"sharedairsname": "东航"
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 21:50:00",
				"dweek": "周六",
				"adate": "2019-05-04 23:55:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票较慢，保证100%出票",
				"stip": null,
				"mtip": "保证出票",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 844,
				"drate": 0.69,
				"ticket": 8
			}],
			"classinfor": [{
				"rmktitle": "退改¥258起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "R",
				"drate": 0.69,
				"display": "经济舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNRjMwMjAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMjE6NTA6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T1",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "HU",
				"airsname": "海航",
				"flgno": "HU7605",
				"ishared": false
			},
			"craftinfo": {
				"craft": "333",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 07:45:00",
				"dweek": "周六",
				"adate": "2019-05-04 10:00:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "93",
				"mtip": "准点率高",
				"info": "93"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均8分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 880,
				"drate": 0.6,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥264起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "M",
				"drate": 0.6,
				"display": "经典经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjA1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjQ1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥298起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.27,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjA1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjQ1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CZ",
				"airsname": "南航",
				"flgno": "CZ3907",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33G",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 08:15:00",
				"dweek": "周六",
				"adate": "2019-05-04 10:30:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "93",
				"mtip": "准点率高",
				"info": "93"
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 920,
				"drate": 0.75,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥276起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "U",
				"drate": 0.75,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ1ozOTA3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjE1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1700,
				"drate": 0.49,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥255起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "D",
				"drate": 0.49,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ1ozOTA3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjE1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MF",
				"airsname": "厦航",
				"flgno": "MF1367",
				"ishared": true,
				"sharedflgno": "CZ3907",
				"sharedairsname": "南航"
			},
			"craftinfo": {
				"craft": "33G",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 08:15:00",
				"dweek": "周六",
				"adate": "2019-05-04 10:30:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "93",
				"mtip": "准点率高",
				"info": "93"
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票较慢，保证100%出票",
				"stip": null,
				"mtip": "保证出票",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 920,
				"drate": 0.75,
				"ticket": 5
			}],
			"classinfor": [{
				"rmktitle": "退改¥276起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "U",
				"drate": 0.75,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTUYxMzY3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjE1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MF",
				"airsname": "厦航",
				"flgno": "MF8178",
				"ishared": false
			},
			"craftinfo": {
				"craft": "738",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 13:05:00",
				"dweek": "周六",
				"adate": "2019-05-04 15:30:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "97",
				"mtip": "准点率高",
				"info": "97"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 920,
				"drate": 0.75,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥276起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "K",
				"drate": 0.75,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTUY4MTc4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEzOjA1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.49,
				"ticket": 1
			}],
			"classinfor": [{
				"rmktitle": "退改¥373起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.49,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTUY4MTc4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEzOjA1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T1",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "HU",
				"airsname": "海航",
				"flgno": "HU7603",
				"ishared": false
			},
			"craftinfo": {
				"craft": "738",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 21:15:00",
				"dweek": "周六",
				"adate": "2019-05-04 23:35:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "77",
				"mtip": "准点率较高",
				"info": "77"
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 945,
				"drate": 0.64,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥189起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "P",
				"drate": 0.64,
				"display": "经典经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjAzIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIxOjE1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1640,
				"drate": 0.29,
				"ticket": 1
			}],
			"classinfor": [{
				"rmktitle": "退改¥164起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.29,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjAzIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIxOjE1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1589",
				"ishared": false
			},
			"craftinfo": {
				"craft": "747",
				"kind": "大",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 20:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 22:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "57",
				"mtip": "准点率较高",
				"info": "57"
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 970,
				"drate": 0.66,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥194起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "V",
				"drate": 0.66,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTg5IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1790,
				"drate": 0.32,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥90起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTg5IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1557",
				"ishared": false
			},
			"craftinfo": {
				"craft": "789",
				"kind": "大",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 11:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 13:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "83",
				"mtip": "准点率高",
				"info": "83"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 980,
				"drate": 0.66,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥196起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "V",
				"drate": 0.66,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTU3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDExOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥75起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTU3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDExOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1857",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33A",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 19:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 21:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "80",
				"mtip": "准点率高",
				"info": "80"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 980,
				"drate": 0.66,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥196起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "V",
				"drate": 0.66,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODU3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE5OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1790,
				"drate": 0.32,
				"ticket": 7
			}],
			"classinfor": [{
				"rmktitle": "退改¥90起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODU3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE5OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5126",
				"ishared": false
			},
			"craftinfo": {
				"craft": "359",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 20:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 22:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "50",
				"mtip": "准点率较高",
				"info": "50"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 980,
				"drate": 0.66,
				"ticket": 4
			}],
			"classinfor": [{
				"rmktitle": "退改¥294起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "N",
				"drate": 0.66,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTI2IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1800,
				"drate": 0.32,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥360起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTI2IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5158",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33H",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 21:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 23:45:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "55",
				"mtip": "准点率较高",
				"info": "55"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 980,
				"drate": 0.66,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥294起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "N",
				"drate": 0.66,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTU4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIxOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1800,
				"drate": 0.32,
				"ticket": 4
			}],
			"classinfor": [{
				"rmktitle": "退改¥360起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTU4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIxOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5152",
				"ishared": false
			},
			"craftinfo": {
				"craft": "32L",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 11:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 14:00:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "80",
				"mtip": "准点率高",
				"info": "80"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 980,
				"drate": 0.66,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥294起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "N",
				"drate": 0.66,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTUyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDExOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1640,
				"drate": 0.29,
				"ticket": 1
			}],
			"classinfor": [{
				"rmktitle": "退改¥328起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.29,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTUyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDExOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MF",
				"airsname": "厦航",
				"flgno": "MF3018",
				"ishared": true,
				"sharedflgno": "MU5158",
				"sharedairsname": "东航"
			},
			"craftinfo": {
				"craft": "33H",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 21:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 23:45:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "55",
				"mtip": "准点率较高",
				"info": "55"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票较慢，保证100%出票",
				"stip": null,
				"mtip": "保证出票",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 994,
				"drate": 0.81,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥196起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "K",
				"drate": 0.81,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTUYzMDE4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIxOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "NAY",
				"aportsname": "南苑",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "KN",
				"airsname": "中联航",
				"flgno": "KN5955",
				"ishared": false
			},
			"craftinfo": {
				"craft": "73V",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 15:50:00",
				"dweek": "周六",
				"adate": "2019-05-04 18:00:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "77",
				"mtip": "准点率较高",
				"info": "77"
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1018,
				"drate": 0.75,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥407起",
				"ifb": "无托运行李额",
				"cgrd": 0,
				"sclass": "H",
				"drate": 0.75,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiS041OTU1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE1OjUwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "FM",
				"airsname": "上航",
				"flgno": "FM9102",
				"ishared": false
			},
			"craftinfo": {
				"craft": "73E",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 20:20:00",
				"dweek": "周六",
				"adate": "2019-05-04 22:50:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "67",
				"mtip": "准点率较高",
				"info": "67"
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1030,
				"drate": 0.84,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥309起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "K",
				"drate": 0.84,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiRk05MTAyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjIwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1800,
				"drate": 0.33,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥360起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.33,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiRk05MTAyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjIwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5154",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 13:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 15:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "73",
				"mtip": "准点率较高",
				"info": "73"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1130,
				"drate": 0.76,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥339起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "L",
				"drate": 0.76,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTU0IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEzOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 4
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTU0IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEzOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1517",
				"ishared": false
			},
			"craftinfo": {
				"craft": "747",
				"kind": "大",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 13:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 15:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "83",
				"mtip": "准点率高",
				"info": "83"
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1130,
				"drate": 0.76,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥226起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "Q",
				"drate": 0.76,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTE3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEzOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1790,
				"drate": 0.32,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥90起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTE3IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEzOjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T1",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "Y8",
				"airsname": "金鹏航空",
				"flgno": "Y87611",
				"ishared": true,
				"sharedflgno": "HU7611",
				"sharedairsname": "海航"
			},
			"craftinfo": {
				"craft": "787",
				"kind": "大",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 07:40:00",
				"dweek": "周六",
				"adate": "2019-05-04 09:55:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "93",
				"mtip": "准点率高",
				"info": "93"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1130,
				"drate": 0.76,
				"ticket": 7
			}],
			"classinfor": [{
				"rmktitle": "退改¥226起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "K",
				"drate": 0.76,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiWTg3NjExIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA3OjQwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5106",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 10:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 12:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "90",
				"mtip": "准点率高",
				"info": "90"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1130,
				"drate": 0.76,
				"ticket": 8
			}],
			"classinfor": [{
				"rmktitle": "退改¥339起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "L",
				"drate": 0.76,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTA2IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEwOjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥298起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTA2IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEwOjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5108",
				"ishared": false
			},
			"craftinfo": {
				"craft": "333",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 11:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 13:20:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "70",
				"mtip": "准点率较高",
				"info": "70"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1130,
				"drate": 0.76,
				"ticket": 8
			}],
			"classinfor": [{
				"rmktitle": "退改¥339起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "L",
				"drate": 0.76,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTA4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDExOjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 6
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTA4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDExOjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5110",
				"ishared": false
			},
			"craftinfo": {
				"craft": "359",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 12:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 14:20:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "90",
				"mtip": "准点率高",
				"info": "90"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1130,
				"drate": 0.76,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥339起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "L",
				"drate": 0.76,
				"display": "经济舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNVTUxMTAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMTI6MDA6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNVTUxMTAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMTI6MDA6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T1",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5130",
				"ishared": false
			},
			"craftinfo": {
				"craft": "323",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 19:35:00",
				"dweek": "周六",
				"adate": "2019-05-04 22:00:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "53",
				"mtip": "准点率较高",
				"info": "53"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1130,
				"drate": 0.76,
				"ticket": 6
			}],
			"classinfor": [{
				"rmktitle": "退改¥339起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "L",
				"drate": 0.76,
				"display": "经济舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNVTUxMzAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMTk6MzU6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNVTUxMzAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMTk6MzU6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "FM",
				"airsname": "上航",
				"flgno": "FM9108",
				"ishared": false
			},
			"craftinfo": {
				"craft": "73L",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 18:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 20:50:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "57",
				"mtip": "准点率较高",
				"info": "57"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1230,
				"drate": 0.99,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥62起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "B",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiRk05MTA4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2720,
				"drate": 0.49,
				"ticket": 1
			}],
			"classinfor": [{
				"rmktitle": "退改¥544起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.49,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiRk05MTA4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T1",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "HU",
				"airsname": "海航",
				"flgno": "HU7609",
				"ishared": false
			},
			"craftinfo": {
				"craft": "333",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 14:45:00",
				"dweek": "周六",
				"adate": "2019-05-04 17:10:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "83",
				"mtip": "准点率高",
				"info": "83"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均8分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1235,
				"drate": 0.83,
				"ticket": 7
			}],
			"classinfor": [{
				"rmktitle": "退改¥247起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "H",
				"drate": 0.83,
				"display": "经典经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjA5IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE0OjQ1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1625,
				"drate": 0.29,
				"ticket": 5
			}],
			"classinfor": [{
				"rmktitle": "退改¥163起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.29,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjA5IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE0OjQ1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1855",
				"ishared": false
			},
			"craftinfo": {
				"craft": "359",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 17:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 19:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "57",
				"mtip": "准点率较高",
				"info": "57"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1280,
				"drate": 0.86,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥128起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "U",
				"drate": 0.86,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODU1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE3OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}, {
			"priceinfo": [{
				"price": 1790,
				"drate": 0.32,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥90起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODU1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE3OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1885",
				"ishared": false
			},
			"craftinfo": {
				"craft": "32A",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 18:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 20:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "80",
				"mtip": "准点率高",
				"info": "80"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1280,
				"drate": 0.86,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥128起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "U",
				"drate": 0.86,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODg1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}, {
			"priceinfo": [{
				"price": 1790,
				"drate": 0.32,
				"ticket": 4
			}],
			"classinfor": [{
				"rmktitle": "退改¥90起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExODg1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5112",
				"ishared": false
			},
			"craftinfo": {
				"craft": "773",
				"kind": "大",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 13:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 15:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "83",
				"mtip": "准点率高",
				"info": "83"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1280,
				"drate": 0.86,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥384起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "K",
				"drate": 0.86,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTEyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEzOjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1640,
				"drate": 0.29,
				"ticket": 5
			}],
			"classinfor": [{
				"rmktitle": "退改¥328起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.29,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTEyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDEzOjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5122",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 18:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 20:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1280,
				"drate": 0.86,
				"ticket": 5
			}],
			"classinfor": [{
				"rmktitle": "退改¥384起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "K",
				"drate": 0.86,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTIyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE4OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTIyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE4OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5124",
				"ishared": false
			},
			"craftinfo": {
				"craft": "333",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 19:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 21:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "50",
				"mtip": "准点率较高",
				"info": "50"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1280,
				"drate": 0.86,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥384起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "K",
				"drate": 0.86,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTI0IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE5OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTI0IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE5OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU9102",
				"ishared": true,
				"sharedflgno": "FM9102",
				"sharedairsname": "上航"
			},
			"craftinfo": {
				"craft": "73E",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 20:20:00",
				"dweek": "周六",
				"adate": "2019-05-04 22:50:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "67",
				"mtip": "准点率较高",
				"info": "67"
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1280,
				"drate": 0.86,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥384起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "K",
				"drate": 0.86,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU5MTAyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjIwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1800,
				"drate": 0.32,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥360起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU5MTAyIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDIwOjIwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T1",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "HU",
				"airsname": "海航",
				"flgno": "HU7601",
				"ishared": false
			},
			"craftinfo": {
				"craft": "350",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 17:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 19:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "60",
				"mtip": "准点率较高",
				"info": "60"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均8分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1355,
				"drate": 0.91,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥271起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "B",
				"drate": 0.91,
				"display": "经典经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjAxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE3OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2665,
				"drate": 0.48,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥267起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "D",
				"drate": 0.48,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiSFU3NjAxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE3OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1521",
				"ishared": false
			},
			"craftinfo": {
				"craft": "330",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 14:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 16:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "87",
				"mtip": "准点率高",
				"info": "87"
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 7
			}],
			"classinfor": [{
				"rmktitle": "免费改期",
				"ifb": "",
				"cgrd": 0,
				"sclass": "Y",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTIxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE0OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥149起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Z",
				"drate": 0.53,
				"display": "超值公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTIxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE0OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1515",
				"ishared": false
			},
			"craftinfo": {
				"craft": "332",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 15:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 17:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "87",
				"mtip": "准点率高",
				"info": "87"
			}, {
				"type": 3,
				"tip": "含小食",
				"stip": "含小食",
				"mtip": "含小食",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "免费改期",
				"ifb": "",
				"cgrd": 0,
				"sclass": "Y",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTE1IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE1OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKqB0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5OAGlJHZlcnNpb24iOiIBeWBlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jCVokc3ViY2hhbm5lbAVpOGlzc2hhcmUiOmZhbHNlfQ=="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1549",
				"ishared": false
			},
			"craftinfo": {
				"craft": "32A",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 16:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 18:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "53",
				"mtip": "准点率较高",
				"info": "53"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "免费改期",
				"ifb": "",
				"cgrd": 0,
				"sclass": "Y",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTQ5IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE2OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 1790,
				"drate": 0.32,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥90起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.32,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTQ5IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE2OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5120",
				"ishared": false
			},
			"craftinfo": {
				"craft": "333",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 17:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 19:15:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "57",
				"mtip": "准点率较高",
				"info": "57"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥74起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "B",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNVTUxMjAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMTc6MDA6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQKoeyJmbm8iOiJNVTUxMjAiLCJkZGF0ZSI6IjIwMTktMDUtMDQgMTc6MDA6MAUeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBYMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSIBWiRzdWJjaGFubmVsBZM4aXNzaGFyZSI6ZmFsc2V9"
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5114",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 14:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 16:20:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "83",
				"mtip": "准点率高",
				"info": "83"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥74起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "B",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTE0IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE0OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 4
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTE0IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE0OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU5116",
				"ishared": false
			},
			"craftinfo": {
				"craft": "33L",
				"kind": "大",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 15:00:00",
				"dweek": "周六",
				"adate": "2019-05-04 17:20:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "80",
				"mtip": "准点率高",
				"info": "80"
			}, {
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥74起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "B",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTE2IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE1OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 3730,
				"drate": 0.66,
				"ticket": 4
			}],
			"classinfor": [{
				"rmktitle": "退改¥746起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "D",
				"drate": 0.66,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU1MTE2IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE1OjAwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU9108",
				"ishared": true,
				"sharedflgno": "FM9108",
				"sharedairsname": "上航"
			},
			"craftinfo": {
				"craft": "73L",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 18:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 20:50:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "",
				"stip": "57",
				"mtip": "准点率较高",
				"info": "57"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "退改¥74起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "B",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU5MTA4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 2980,
				"drate": 0.53,
				"ticket": 1
			}],
			"classinfor": [{
				"rmktitle": "退改¥596起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "Q",
				"drate": 0.53,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiTVU5MTA4IiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T1",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU271",
				"ishared": false
			},
			"craftinfo": {
				"craft": "321",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 12:55:00",
				"dweek": "周六",
				"adate": "2019-05-04 15:20:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "90",
				"mtip": "准点率高",
				"info": "90"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥74起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "B",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gAKoeyJmbm8iOiJNVTI3MSIsImRkYXRlIjoiMjAxOS0wNS0wNCAxMjo1NTowMAEeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBmMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSI6MCwic3ViY2hhbm5lbAWTOGlzc2hhcmUiOmZhbHNlfQ=="
		}, {
			"priceinfo": [{
				"price": 2240,
				"drate": 0.4,
				"ticket": 2
			}],
			"classinfor": [{
				"rmktitle": "退改¥448起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "I",
				"drate": 0.4,
				"display": "公务舱"
			}],
			"pid": "gAKoeyJmbm8iOiJNVTI3MSIsImRkYXRlIjoiMjAxOS0wNS0wNCAxMjo1NTowMAEeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBmMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSI6MCwic3ViY2hhbm5lbAWTOGlzc2hhcmUiOmZhbHNlfQ=="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1583",
				"ishared": false
			},
			"craftinfo": {
				"craft": "738",
				"kind": "中",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 16:05:00",
				"dweek": "周六",
				"adate": "2019-05-04 18:30:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均5分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1480,
				"drate": 0.99,
				"ticket": 10
			}],
			"classinfor": [{
				"rmktitle": "免费改期",
				"ifb": "",
				"cgrd": 0,
				"sclass": "Y",
				"drate": 0.99,
				"display": "经济舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTgzIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE2OjA1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}, {
			"priceinfo": [{
				"price": 4170,
				"drate": 0.74,
				"ticket": 1
			}],
			"classinfor": [{
				"rmktitle": "退改¥209起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "C",
				"drate": 0.74,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTgzIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDE2OjA1OjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T3",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "SHA",
				"aportsname": "虹桥",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T2",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "CA",
				"airsname": "国航",
				"flgno": "CA1501",
				"ishared": false
			},
			"craftinfo": {
				"craft": "773",
				"kind": "大",
				"cname": "波音"
			},
			"dateinfo": {
				"ddate": "2019-05-04 08:30:00",
				"dweek": "周六",
				"adate": "2019-05-04 10:40:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 2,
				"tip": "航班准点率高，跟延误说再见",
				"stip": "87",
				"mtip": "准点率高",
				"info": "87"
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 1,
				"tip": "大机型座位宽，飞行更平稳不颠簸",
				"stip": "大机型",
				"mtip": "舒适宽体机",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均4分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1490,
				"drate": 0.27,
				"ticket": 5
			}],
			"classinfor": [{
				"rmktitle": "退改¥75起",
				"ifb": "",
				"cgrd": 2,
				"sclass": "R",
				"drate": 0.27,
				"display": "公务舱"
			}],
			"pid": "gQLwPnsiZm5vIjoiQ0ExNTAxIiwiZGRhdGUiOiIyMDE5LTA1LTA0IDA4OjMwOjAwIiwiZGNpdHkiOiJCSlMiLCJhYwkOXFNIQSIsInByaWNlIjowLjAsInNnbiI6MAEUCHR5cAEVECwid2V3DR0AdC4qAAh2dHkFKth0aWQiOiI4OWQ5MjMzNC0wZDZhLTQ4NTktOTJhZi02YjQ4Njk0OGU5ODUiLCJ2ZXJzaW9uIjoiAXlgZWZsYWciOmZhbHNlLCJGbGlnaHRBZ2VuYwlaJHN1YmNoYW5uZWwFaThpc3NoYXJlIjpmYWxzZX0="
		}],
		"fltoday": 0
	}, {
		"mutilstn": [{
			"dportinfo": {
				"aport": "PEK",
				"aportsname": "首都",
				"cityname": "北京",
				"city": "BJS",
				"bsname": "T2",
				"cityid": "1"
			},
			"aportinfo": {
				"aport": "PVG",
				"aportsname": "浦东",
				"cityname": "上海",
				"city": "SHA",
				"bsname": "T1",
				"cityid": "2"
			},
			"basinfo": {
				"aircode": "MU",
				"airsname": "东航",
				"flgno": "MU563",
				"ishared": false
			},
			"craftinfo": {
				"craft": "325",
				"kind": "中",
				"cname": "空客"
			},
			"dateinfo": {
				"ddate": "2019-05-04 17:15:00",
				"dweek": "周六",
				"adate": "2019-05-04 19:30:00",
				"aweek": "周六",
				"doday": 0,
				"aoday": 0
			},
			"fsitem": [],
			"isstop": false,
			"comlist": [{
				"type": 4,
				"tip": "免费WIFI, 机上上网更便捷",
				"stip": "有WIFI",
				"mtip": "机上有Wi-Fi",
				"info": null
			}, {
				"type": 3,
				"tip": "含正餐",
				"stip": "含正餐",
				"mtip": "含正餐",
				"info": null
			}, {
				"type": 5,
				"tip": "出票快：支付后平均2分钟内完成出票",
				"stip": null,
				"mtip": "出票速度快",
				"info": null
			}],
			"tnote": ""
		}],
		"policyinfo": [{
			"priceinfo": [{
				"price": 1490,
				"drate": 1.0,
				"ticket": 3
			}],
			"classinfor": [{
				"rmktitle": "退改¥75起",
				"ifb": "",
				"cgrd": 0,
				"sclass": "Y",
				"drate": 1.0,
				"display": "经济舱"
			}],
			"pid": "gAKoeyJmbm8iOiJNVTU2MyIsImRkYXRlIjoiMjAxOS0wNS0wNCAxNzoxNTowMAEeNGNpdHkiOiJCSlMiLCJhDQ5cU0hBIiwicHJpY2UiOjAuMCwic2duIjowARQIdHlwARUQLCJ3ZXcNHQB0LioAAHYBUPBmMCwidGlkIjoiODlkOTIzMzQtMGQ2YS00ODU5LTkyYWYtNmI0ODY5NDhlOTg1IiwidmVyc2lvbiI6IkEiLCJlZmxhZyI6ZmFsc2UsIkZsaWdodEFnZW5jeSI6MCwic3ViY2hhbm5lbAWTOGlzc2hhcmUiOmZhbHNlfQ=="
		}],
		"fltoday": 0
	}],
	"airports": [{
		"aport": "PVG",
		"aportsname": "上海浦东国际机场",
		"cityname": null,
		"city": null,
		"bsname": null,
		"cityid": null
	}, {
		"aport": "PEK",
		"aportsname": "北京首都国际机场",
		"cityname": null,
		"city": null,
		"bsname": null,
		"cityid": null
	}, {
		"aport": "NAY",
		"aportsname": "北京南苑机场",
		"cityname": null,
		"city": null,
		"bsname": null,
		"cityid": null
	}, {
		"aport": "SHA",
		"aportsname": "上海虹桥国际机场",
		"cityname": null,
		"city": null,
		"bsname": null,
		"cityid": null
	}],
	"airlines": [{
		"aircode": "KN",
		"airsname": "中国联航"
	}, {
		"aircode": "HO",
		"airsname": "吉祥航空"
	}, {
		"aircode": "CZ",
		"airsname": "南方航空"
	}, {
		"aircode": "FM",
		"airsname": "上海航空"
	}, {
		"aircode": "MU",
		"airsname": "东方航空"
	}, {
		"aircode": "MF",
		"airsname": "厦门航空"
	}, {
		"aircode": "HU",
		"airsname": "海南航空"
	}, {
		"aircode": "CA",
		"airsname": "中国国航"
	}, {
		"aircode": "Y8",
		"airsname": "金鹏航空"
	}],
	"rlt": 0,
	"rltmsg": "北京|上海",
	"recomd": [],
	"dfcnt": 60,
	"hastab": false,
	"rstype": 1,
	"segno": 1
}
"""
ret = json.loads(data)
with open('./xc.txt', 'a', encoding='utf-8') as f:
    f.write(str(ret))
f.close()