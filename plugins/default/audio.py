if answ[1] == 'музыка':
	if (answ_text == ''):
		apisay('Запрос я вводить должна?',toho,torep)
	else:
		param = (('v', '5.63'), ('q',answ_text),('count','300'),('sort','2'),('access_token',token),('forward_messages',torep))
		res = requests.post('https://api.vk.com/method/audio.search', data=param)
		res = json.loads(res.text)
		fcount = 0
		info = ''
		if (res['response']['count'] != 0 ):
			for k in range(len(res['response']['items'])):
				if(fcount == 10):
					break
				info = info+'audio'+str(res['response']['items'][k]['owner_id'])+'_'+str(res['response']['items'][k]['id'])+','
				fcount += 1
		param = (('v', '5.63'), ('q',answ_text),('count','300'),('sort','0'),('access_token',token),('forward_messages',torep))
		res = requests.post('https://api.vk.com/method/audio.search', data=param)
		res = json.loads(res.text)
		if (res['response']['count'] !=0 ):
			for k in range(len(res['response']['items'])):
				if(fcount == 10):
					break
				info = info+'audio'+str(res['response']['items'][k]['owner_id'])+'_'+str(res['response']['items'][k]['id'])+','
				fcount += 1

			param = (('v', '5.74'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Вот, как вы и просили:'),('attachment',info))
			requests.post('https://api.vk.com/method/messages.send', data=param)
		else:
			apisay('Ничего не найдено:с',toho,torep)
