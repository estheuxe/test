import requests

url = 'https://api.tracker.yandex.net'
token = 'OAuth AgAAAAA32rkWAAXfItnToFl5-khFhmcxBlv_R-M'
orgId = '3324002'

uri = 'https://api.tracker.yandex.net/v2/boards'

hdrs = {
	'Host': url,
	'Authorization': token,
	'X-Org-ID': orgId
}

response = requests.request('GET', uri, headers=hdrs)

print(response.status_code)
print()
print(response.text)