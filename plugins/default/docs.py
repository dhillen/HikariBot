if answ[1] == 'доки':
	param = (('v', '5.68'), ('q',answ_text),('count','100'),('access_token',token),('forward_messages',torep))
	res = requests.post('https://api.vk.com/method/docs.search', data=param).json()
	info = ''
	
	if (res['response']['count'] != 0 ):
		for k in range(len(res['response']['items'])):
			for i in range(10):
				itm = random.randint( 0, len(res['response']['items'])-1)
				
				if res['response']['items'][itm]['id'] in (474084484,444393573,337586976,467187768,170067184,170126360,457132116,453208914,464271002,474084484,463015737,11290494,329510426,122229518,459118885):
					continue
				if res['response']['items'][itm]['title'].lower().find('theync') != -1:
					continue
				if res['response']['items'][itm]['title'].lower().find('1man1jar') != -1:
					continue
				info = info+'doc'+str(res['response']['items'][itm]['owner_id'])+'_'+str(res['response']['items'][itm]['id'])+','

		param = (('v', '5.74'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Доки по вашему запросу:'),('attachment',info))
		requests.post('https://api.vk.com/method/messages.send', data=param)
	else:
		apisay('Документы по запросу не найдены',toho,torep)

if answ[1] == 'гиф':
	param = (('v', '5.68'), ('q',answ_text),('count','100'),('access_token',token),('forward_messages',torep))
	res = requests.post('https://api.vk.com/method/docs.search', data=param).json()
	info = ''
	
	if (res['response']['count'] != 0 ):
		for k in range(len(res['response']['items'])):
			for i in range(10):
				itm = random.randint( 0, len(res['response']['items'])-1)
				if res['response']['items'][itm]['id'] in (474084484,444393573,337586976,467187768,170067184,170126360,457132116,453208914,464271002,474084484,463015737,11290494,329510426,122229518,459118885):
					continue
				if res['response']['items'][itm]['title'].lower().find('theync') != -1:
					continue
				if res['response']['items'][itm]['title'].lower().find('1man1jar') != -1:
					continue
				
				if res['response']['items'][itm]['ext']==('gif'):
					info = info+'doc'+str(res['response']['items'][itm]['owner_id'])+'_'+str(res['response']['items'][itm]['id'])+','
	

		param = (('v', '5.74'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Доки по вашему запросу:'),('attachment',info))
		requests.post('https://api.vk.com/method/messages.send', data=param)
	else:
		apisay('Гифки по запросу не найдены',toho,torep)

if answ[1] == 'фото':
	param = (('v', '5.68'), ('q',answ_text),('count','100'),('access_token',token),('forward_messages',torep))
	res = requests.post('https://api.vk.com/method/photos.search', data=param).json()
	info = ''
	
	if (res['response']['count'] != 0 ):
		for k in range(len(res['response']['items'])):
			for i in range(10):
				itm = random.randint( 0, len(res['response']['items'])-1)
				info = info+'photo'+str(res['response']['items'][itm]['owner_id'])+'_'+str(res['response']['items'][itm]['id'])+','

		param = (('v', '5.74'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Доки по вашему запросу:'),('attachment',info))
		requests.post('https://api.vk.com/method/messages.send', data=param)
	else:
		apisay('Фотографии по запросу не найдены',toho,torep)
