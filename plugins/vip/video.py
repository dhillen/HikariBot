if answ[1] == 'видео':
		param = (('v', '5.68'), ('q',answ_text),('count','10'),('access_token',token),('adult','1'),('forward_messages',torep))
		res = requests.post('https://api.vk.com/method/video.search', data=param).json()
		info = ''

		if (res['response']['count'] != 0):
			for k in range(len(res['response']['items'])):
				for i in range(10):
					itm = random.randint( 0, res['response']['count'])
					title = res['response']['items'][itm]['title'].lower()
					
					if res['response']['items'][itm]['id'] in (170754590,170631958,170067184,168063882,160911967,140239214,1609119666,166873080,166873080,166873080,166873080,166873080,166873080,166873080,160973038,166088674,166159461,456239165,159490950,169336720,169712331,169875157,159555698):
						continue
					if (title.find('банк') != -1) and (title.find('жоп') != -1):
						continue
					if (title.find('банк') != -1) and (title.find('сел') != -1):
						continue
					if (title.find('банк') != -1) and (title.find('мужик') != -1):
						continue
					if (title.find('мужик') != -1) and (title.find('сел') != -1):
						continue
					if (title.find('guy') != -1) and (title.find('cup') != -1):
						continue
					if (title.find('cup') != -1) and (title.find('guy') != -1):
						continue
					if title.find('theync') != -1:
						continue
	
				info = info+'video'+str(res['response']['items'][itm]['owner_id'])+'_'+str(res['response']['items'][itm]['id'])+','
		
			param = (('v', '5.68'), ('peer_id',toho),('access_token',token),('forward_messages',torep),('message','Видео по вашему запросу'),('attachment',info))
			requests.post('https://api.vk.com/method/messages.send', data=param)
		else:
			apisay('Видео по запросу не найдены.',toho,torep)
