if answ[1] == 'музр':
	param = (('v', '5.63'), ('q',answ_text),('count','300'),('sort','2'),('access_token',token),('forward_messages',torep))
	res = requests.post('https://api.vk.com/method/audio.search', data=param).json()
	info = ''

	if (res['response']['count'] != 0 ):
		for k in range(len(res['response']['items'])):
			itm = random.randint( 0, len(res['response']['items'])-1)
			info = info+'audio'+str(res['response']['items'][itm]['owner_id'])+'_'+str(res['response']['items'][itm]['id'])+','

		param = (('v', '5.74'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Вот, как вы и просили:'),('attachment',info))
		requests.post('https://api.vk.com/method/messages.send', data=param)
	else:
		apisay('Ничего не найдено:с',toho,torep)
