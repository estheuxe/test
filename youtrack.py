import requests
import json

uriUsers = 'https://estheuxework.myjetbrains.com/youtrack/api/admin/users/me'
uriCustomField = 'https://estheuxework.myjetbrains.com/youtrack/api/admin/customFieldSettings/customFields'
uriProjectCustomField = 'https://estheuxework.myjetbrains.com/youtrack/api/admin/projects/0-0/customFields'
uri = 'https://estheuxework.myjetbrains.com/youtrack/api/issues'
uriEdit = 'https://estheuxework.myjetbrains.com/youtrack/api/issues/{id}'

prj = 'https://estheuxework.myjetbrains.com/youtrack/api/admin/projects'

# permanent
token = 'perm:cm9vdA==.NDYtMQ==.UQ5xwQt0IXO6fZUB5hGtRS1DulxQSN'

hdrs = {
	'Authorization': 'Bearer perm:cm9vdA==.NDYtMQ==.UQ5xwQt0IXO6fZUB5hGtRS1DulxQSN',
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'Cache-Control': 'no-cache'
}

qs = {
	'fields': 'id,name,login,email'
}

qs1 = {
	'fields': 'id,name,aliases,instances(id,project(id,name))'
}

qs2 = {
	'fields': 'id,canBeEmpty,emptyFieldText,project(id,name),field(id,name)'
}

fields = {
	'fields': 'id,summary,name,description,reporter(login)'
}

flds = {
	'fields': 'idReadable'
}

json = {
	'summary': 'from youtrack.py',
	'description': 'desc from yt.py',
	'project': {
		'id': '0-0',
	}
}

fields123 = {
	'fields': 'id,summary,customFields(id,name,value(avatarUrl,buildLink,color(id),fullName,id,isResolved,localizedName,login,minutes,name,presentation,text))'
}

json123 = {
	'summary': 'Abrakadabra',
	'description': 'I ya toje'
}

idCard = 'P1-2'
#response = requests.request('GET', uri, params=fields, headers=hdrs)

#print(json.dumps(response.json(), indent=4))

resp = requests.request('GET', prj, headers=hdrs, params={'fields': 'name,id'})

#print(json.dumps(resp.json(),indent=4))
print(resp.json())