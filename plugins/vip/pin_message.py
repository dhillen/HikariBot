if answ[1] == 'закрепи':
	try:
		id = ''
		param = (('v','5.68'),('access_token',token),('message_ids',torep, ),('fields', 'id'))
		ret = requests.post('https://api.vk.com/method/messages.getById',data = param).text
		date = json.loads(ret)['response']['items'][0]['fwd_messages'][0]['date']
		body = json.loads(ret)['response']['items'][0]['fwd_messages'][0]['body']
		

		param = (('v','5.68'),('access_token',token),('q', body),('peer_id', toho))
		ret = requests.post('https://api.vk.com/method/messages.search',data = param).text
		search = json.loads(ret)

		for i in range(search['response']['count']):
			if search['response']['items'][i]['date'] == date and search['response']['items'][i]['body'] == body:
				id = search['response']['items'][i]['id']

		result = requests.post('https://api.vk.com/method/messages.pin?access_token='+str(token)+'&v=5.68', params={'peer_id': str(toho), 'message_id': str(id)})
		
		if result.json()['error']['error_code'] == 925:
			apisay('Админку не дали :(', toho, torep)
	except:
		pass