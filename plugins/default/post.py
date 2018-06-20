def attachment(text, toho, owner_id, media_id):
	param = (('v', '5.68'), ('peer_id', toho),('access_token',token),('message',text),('attachment', 'wall'+str(owner_id)+'_'+str(media_id)))
	result = requests.post('https://api.vk.com/method/messages.send', data=param)

	return result.text
	
if answ[1] == 'пост':
	groups = json.load(open('system/cfg/post','r'))
	domain = ''
	
	try:
		if answ[2] == 'чулочки':
			domain = random.choice(groups['fap'])
		elif answ[2] == 'бугурт':
			domain = random.choice(groups['bugurt'])
		elif answ[2] == 'си':
			domain = random.choice(groups['sbrod'])
		elif answ[2] == 'хентай':
			domain = random.choice(groups['hentai'])
		elif answ[2] == 'юморсека':
			domain = random.choice(groups['humor'])
		else:
			domain = random.choice(groups['humor'])
			#apisay('Введи свой запрос верно',toho,'') #почему то с ответом идёт первый пост со стены бота можно как рекламу юзать ¯\_(ツ)_/¯
		
		get_count = requests.get('https://api.vk.com/method/wall.get?access_token='+str(token)+'&v=5.68', params={'domain': domain})
		max = get_count.json()['response']['count']
		result = requests.get('https://api.vk.com/method/wall.get?access_token='+str(token)+'&v=5.68', params={'domain': domain, 'count':str(max), 'offset':str(random.randint(0, max))})
			
		owner_id = result.json()['response']['items'][0]['owner_id']
		media_id = result.json()['response']['items'][0]['id']
		text = result.json()['response']['items'][0]['text']
			
		attachment(text, toho, owner_id, media_id)
	except:
		apisay('Что-то пошло не так¯\_(ツ)_/¯', toho, torep)
if answ[1] == 'рандом':
	apisay(open('files/txt/random','r').read(),toho,'')