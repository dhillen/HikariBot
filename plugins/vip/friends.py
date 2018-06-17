if answ[1] == 'добавь' and answ[2] == 'друга':
	if (toho > 2000000000):
		friends = requests.get('https://api.vk.com/method/friends.get?access_token='+str(token)+'&v=5.68').json()
		
		max = friends['response']['count']
		id = friends['response']['items'][random.randint(0, max-1)]
		chat_id = str(toho)
		
		req = requests.get('https://api.vk.com/method/messages.addChatUser?access_token='+str(token)+'&v=5.68&chat_id='+chat_id[1::]+'&user_id='+str(id))
		
		time.sleep(2.5)
		
		apisay('Ты был призван Великим рандомом!', toho, torep)
	else:
		apisay('В личке не могу!', toho, '')
	