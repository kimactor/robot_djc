#/usr/bin/env python
#coding=utf-8
import os
import urllib
import urllib2
import re
import cookielib
import json


def jsonPost(info = ""):
	url = "http://www.tuling123.com/openapi/api"
	headers = {}
	headers['Content-Type'] = 'application/json; charset=utf-8'
	values = {}
	values["key"] = '8dbb03717c2045449b90639082a1a0aa'
	values['info'] = info
	values['loc'] = "深圳市南山区"
	values['userid'] = "123456"

	post_data = urllib.urlencode(values)
	j_data = json.dumps(values)
	req = urllib2.Request(url, j_data, headers)
	page = urllib2.urlopen(req)
	res = page.read()
	page.close()
	return eval(res)['text']

res = jsonPost("")
print res
