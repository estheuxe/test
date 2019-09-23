import requests, json

uri = 'https://ru.wikipedia.org/wiki/HTTP'

querystring = {
	'Host': 'ru.wikipedia.org',
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5',
	'Accept': 'text/html',
	'Connection': 'close'
}

response = requests.request("GET", uri, params=querystring)

print(response.text)

#print(json.dumps(response.json(), indent=4))