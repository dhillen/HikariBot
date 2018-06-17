def check_id(chat_id):
	friends = requests.get('https://api.vk.com/method/friends.get?access_token='+str(token)+'&v=5.68').json()
	users = requests.get('https://api.vk.com/method/messages.getChat?access_token='+str(token)+'&v=5.68&chat_id='+chat_id)
	max = friends['response']['count']
	id = friends['response']['items'][random.randint(0, max-1)]
		
	for n in range(10):
		if id not in users.json()['response']['users']:
			return str(id)
		else:
			id = friends['response']['items'][random.randint(0, max-1)]
	
	return 'false'


if answ[1] == 'добавь' and answ[2] == 'друга':	
	if (toho > 2000000000):
		chat_id = str(toho)
		
		id = check_id(chat_id[1::])
		
		if id != 'false':
			print(id)
			req = requests.get('https://api.vk.com/method/messages.addChatUser?access_token='+str(token)+'&v=5.68&chat_id='+chat_id[1::]+'&user_id='+id)
			
			time.sleep(1.5)
			
			apisay('Ты был призван Великим рандомом!', toho, torep)
	else:
		apisay('В личке не могу!', toho, '')
	